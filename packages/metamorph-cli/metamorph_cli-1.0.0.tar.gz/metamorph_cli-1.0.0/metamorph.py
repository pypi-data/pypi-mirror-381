#!/usr/bin/env python3
"""
Metadata Editor CLI Tool
A cross-platform tool to view and edit metadata for various file types.
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
import json
import subprocess
import platform

try:
    import PyPDF2
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    PyPDF2 = None

try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except ImportError:
    Image = None

try:
    from mutagen import File as MutagenFile
    from mutagen.easyid3 import EasyID3
    from mutagen.mp3 import MP3
    from mutagen.mp4 import MP4
    from mutagen.flac import FLAC
except ImportError:
    MutagenFile = None


class MetadataEditor:
    """Main class for handling metadata operations."""

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        self.file_type = self._detect_file_type()

    def _detect_file_type(self):
        """Detect file type based on extension."""
        ext = self.file_path.suffix.lower()

        if ext == '.pdf':
            return 'pdf'
        elif ext in ['.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif']:
            return 'image'
        elif ext in ['.mp3', '.mp4', '.m4a', '.flac', '.ogg', '.wav']:
            return 'audio'
        else:
            return 'general'

    def _read_extended_attributes(self):
        """Read extended attributes (macOS/Linux)."""
        result = {}

        try:
            if platform.system() == 'Darwin':  # macOS
                # Read "Where from" attribute using mdls (more reliable)
                try:
                    output = subprocess.run(
                        ['mdls', '-name', 'kMDItemWhereFroms', '-raw', str(self.file_path)],
                        capture_output=True,
                        text=True
                    )
                    if output.returncode == 0 and output.stdout.strip():
                        where_from = self._parse_mdls_array(output.stdout)
                        if where_from:
                            result['WhereFrom'] = where_from
                except Exception:
                    pass

                # Read Finder comment
                try:
                    output = subprocess.run(
                        ['xattr', '-p', 'com.apple.metadata:kMDItemFinderComment', str(self.file_path)],
                        capture_output=True,
                        text=True
                    )
                    if output.returncode == 0 and output.stdout.strip():
                        result['FinderComment'] = output.stdout.strip()
                except Exception:
                    pass

                # Read Finder tags
                try:
                    output = subprocess.run(
                        ['xattr', '-p', 'com.apple.metadata:_kMDItemUserTags', str(self.file_path)],
                        capture_output=True,
                        text=True
                    )
                    if output.returncode == 0 and output.stdout.strip():
                        tags = self._parse_finder_tags(output.stdout)
                        if tags:
                            result['FinderTags'] = ', '.join(tags)
                except Exception:
                    pass

            elif platform.system() == 'Linux':
                # Read all extended attributes on Linux
                try:
                    output = subprocess.run(
                        ['getfattr', '-d', str(self.file_path)],
                        capture_output=True,
                        text=True
                    )
                    if output.returncode == 0:
                        for line in output.stdout.split('\n'):
                            if '=' in line:
                                key, value = line.split('=', 1)
                                result[f'xattr_{key.strip()}'] = value.strip().strip('"')
                except Exception:
                    pass

        except Exception:
            pass

        return result

    def _parse_mdls_array(self, mdls_output):
        """Parse mdls array output."""
        try:
            import urllib.parse
            import re

            # mdls -raw outputs arrays as: (null) or the raw value
            if '(null)' in mdls_output:
                return None

            # If it's a simple string (single value), return it
            if not mdls_output.startswith('('):
                value = mdls_output.strip()
                if value and value != '(null)':
                    return urllib.parse.unquote(value)
                return None

            # Extract first URL from array format
            # Format: ("url1", "url2")
            match = re.search(r'"([^"]+)"', mdls_output)
            if match:
                url = match.group(1)
                return urllib.parse.unquote(url)

        except Exception:
            pass
        return None

    def _parse_finder_tags(self, plist_data):
        """Parse Finder tags from plist data."""
        try:
            import re
            # Extract tag names from the binary plist
            tags = re.findall(r'([A-Za-z0-9\s]+)\n?\d*\n', plist_data)
            if tags:
                return [tag.strip() for tag in tags if tag.strip() and len(tag.strip()) > 1]
        except Exception:
            pass
        return []

    def _write_extended_attributes(self, metadata_dict):
        """Write extended attributes (macOS/Linux)."""
        success = False
        messages = []

        try:
            if platform.system() == 'Darwin':  # macOS
                # Write "Where from" attribute
                if 'WhereFrom' in metadata_dict:
                    try:
                        value = metadata_dict['WhereFrom']
                        if value:
                            # Create a simple plist with the URL
                            import plistlib
                            plist_data = plistlib.dumps([value])
                            result = subprocess.run(
                                ['xattr', '-w', 'com.apple.metadata:kMDItemWhereFroms',
                                 plist_data.hex(), str(self.file_path)],
                                capture_output=True
                            )
                            if result.returncode == 0:
                                success = True
                                messages.append("WhereFrom updated")
                        else:
                            # Remove the attribute if empty
                            subprocess.run(
                                ['xattr', '-d', 'com.apple.metadata:kMDItemWhereFroms',
                                 str(self.file_path)],
                                capture_output=True
                            )
                            success = True
                            messages.append("WhereFrom cleared")
                    except Exception as e:
                        messages.append(f"WhereFrom update failed: {str(e)}")

                # Write Finder comment
                if 'FinderComment' in metadata_dict:
                    try:
                        value = metadata_dict['FinderComment']
                        if value:
                            result = subprocess.run(
                                ['xattr', '-w', 'com.apple.metadata:kMDItemFinderComment',
                                 value, str(self.file_path)],
                                capture_output=True
                            )
                            if result.returncode == 0:
                                success = True
                                messages.append("FinderComment updated")
                        else:
                            subprocess.run(
                                ['xattr', '-d', 'com.apple.metadata:kMDItemFinderComment',
                                 str(self.file_path)],
                                capture_output=True
                            )
                            success = True
                            messages.append("FinderComment cleared")
                    except Exception as e:
                        messages.append(f"FinderComment update failed: {str(e)}")

        except Exception:
            pass

        return success, '; '.join(messages) if messages else None

    def read_metadata(self):
        """Read metadata based on file type."""
        result = {}

        # Always read extended attributes first (macOS/Linux)
        xattr_data = self._read_extended_attributes()
        if xattr_data:
            result.update(xattr_data)

        # Then read file-type-specific metadata
        if self.file_type == 'pdf':
            result.update(self._read_pdf_metadata())
        elif self.file_type == 'image':
            result.update(self._read_image_metadata())
        elif self.file_type == 'audio':
            result.update(self._read_audio_metadata())
        else:
            result.update(self._read_general_metadata())

        return result

    def _read_pdf_metadata(self):
        """Read PDF metadata."""
        if PyPDF2 is None:
            return {"error": "PyPDF2 not installed. Install with: pip install PyPDF2"}

        try:
            reader = PdfReader(str(self.file_path))
            metadata = reader.metadata

            result = {}
            if metadata:
                for key, value in metadata.items():
                    clean_key = key.replace('/', '') if key.startswith('/') else key
                    result[clean_key] = str(value) if value else ""

            # Add page count
            result['PageCount'] = len(reader.pages)

            return result
        except Exception as e:
            return {"error": f"Failed to read PDF metadata: {str(e)}"}

    def _read_image_metadata(self):
        """Read image EXIF metadata."""
        if Image is None:
            return {"error": "Pillow not installed. Install with: pip install Pillow"}

        try:
            img = Image.open(str(self.file_path))
            result = {
                'Format': img.format,
                'Size': f"{img.width}x{img.height}",
                'Mode': img.mode,
            }

            # Get EXIF data
            exif_data = img.getexif()
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    result[str(tag)] = str(value)

            return result
        except Exception as e:
            return {"error": f"Failed to read image metadata: {str(e)}"}

    def _read_audio_metadata(self):
        """Read audio file metadata."""
        if MutagenFile is None:
            return {"error": "Mutagen not installed. Install with: pip install mutagen"}

        try:
            audio = MutagenFile(str(self.file_path))
            if audio is None:
                return {"error": "Unsupported audio format"}

            result = {}

            # Get basic info
            if hasattr(audio.info, 'length'):
                result['Duration'] = f"{int(audio.info.length)} seconds"
            if hasattr(audio.info, 'bitrate'):
                result['Bitrate'] = f"{audio.info.bitrate} bps"
            if hasattr(audio.info, 'sample_rate'):
                result['SampleRate'] = f"{audio.info.sample_rate} Hz"

            # Get tags
            if audio.tags:
                for key, value in audio.tags.items():
                    result[str(key)] = str(value[0]) if isinstance(value, list) else str(value)

            return result
        except Exception as e:
            return {"error": f"Failed to read audio metadata: {str(e)}"}

    def _read_general_metadata(self):
        """Read general file attributes."""
        try:
            stat = self.file_path.stat()
            result = {
                'FileName': self.file_path.name,
                'FileSize': f"{stat.st_size} bytes",
                'Created': datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
                'Modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'Accessed': datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S'),
                'Permissions': oct(stat.st_mode)[-3:],
            }
            return result
        except Exception as e:
            return {"error": f"Failed to read file metadata: {str(e)}"}

    def write_metadata(self, metadata_dict):
        """Write metadata based on file type."""
        # First handle extended attributes
        xattr_success, xattr_msg = self._write_extended_attributes(metadata_dict)

        # Then handle file-type-specific metadata
        if self.file_type == 'pdf':
            success, msg = self._write_pdf_metadata(metadata_dict)
        elif self.file_type == 'image':
            success, msg = self._write_image_metadata(metadata_dict)
        elif self.file_type == 'audio':
            success, msg = self._write_audio_metadata(metadata_dict)
        else:
            success, msg = self._write_general_metadata(metadata_dict)

        # Combine messages
        messages = []
        if xattr_msg:
            messages.append(xattr_msg)
        if msg:
            messages.append(msg)

        combined_msg = '; '.join(messages) if messages else "Metadata updated"
        return success or xattr_success, combined_msg

    def _write_pdf_metadata(self, metadata_dict):
        """Write PDF metadata."""
        if PyPDF2 is None:
            return False, "PyPDF2 not installed"

        try:
            reader = PdfReader(str(self.file_path))
            writer = PdfWriter()

            # Copy all pages
            for page in reader.pages:
                writer.add_page(page)

            # Set metadata
            metadata_to_write = {}
            for key, value in metadata_dict.items():
                if key not in ['PageCount', 'error']:  # Skip read-only fields
                    metadata_to_write[f'/{key}'] = value

            writer.add_metadata(metadata_to_write)

            # Write to temporary file first
            temp_path = self.file_path.with_suffix('.tmp')
            with open(temp_path, 'wb') as output_file:
                writer.write(output_file)

            # Replace original file
            temp_path.replace(self.file_path)

            return True, "PDF metadata updated successfully"
        except Exception as e:
            return False, f"Failed to write PDF metadata: {str(e)}"

    def _write_image_metadata(self, metadata_dict):
        """Write image EXIF metadata."""
        return False, "Image metadata editing not fully supported yet. Use specialized tools for EXIF editing."

    def _write_audio_metadata(self, metadata_dict):
        """Write audio file metadata."""
        if MutagenFile is None:
            return False, "Mutagen not installed"

        try:
            audio = MutagenFile(str(self.file_path))
            if audio is None:
                return False, "Unsupported audio format"

            # Common tag mappings
            common_tags = ['title', 'artist', 'album', 'date', 'genre', 'tracknumber']

            for key, value in metadata_dict.items():
                if key.lower() in common_tags:
                    audio[key.lower()] = value
                elif key not in ['Duration', 'Bitrate', 'SampleRate', 'error']:  # Skip read-only
                    audio[key] = value

            audio.save()
            return True, "Audio metadata updated successfully"
        except Exception as e:
            return False, f"Failed to write audio metadata: {str(e)}"

    def _write_general_metadata(self, metadata_dict):
        """Write general file attributes."""
        try:
            # Only modify timestamps and permissions
            if 'Modified' in metadata_dict:
                try:
                    mtime = datetime.strptime(metadata_dict['Modified'], '%Y-%m-%d %H:%M:%S').timestamp()
                    atime = self.file_path.stat().st_atime
                    os.utime(self.file_path, (atime, mtime))
                except ValueError:
                    pass

            if 'Permissions' in metadata_dict:
                try:
                    mode = int(metadata_dict['Permissions'], 8)
                    os.chmod(self.file_path, mode)
                except ValueError:
                    pass

            return True, "File attributes updated successfully"
        except Exception as e:
            return False, f"Failed to write file metadata: {str(e)}"


def display_metadata(metadata):
    """Display metadata in a readable format."""
    if 'error' in metadata:
        print(f"\nError: {metadata['error']}")
        return

    print("\n" + "="*50)
    print("CURRENT METADATA")
    print("="*50)

    max_key_length = max(len(str(k)) for k in metadata.keys())

    for key, value in metadata.items():
        print(f"{key:<{max_key_length}} : {value}")

    print("="*50)


def interactive_edit(editor):
    """Interactive metadata editing."""
    metadata = editor.read_metadata()

    if 'error' in metadata:
        print(f"\nError: {metadata['error']}")
        return

    display_metadata(metadata)

    print("\nEnter new values for metadata fields (press Enter to keep current value, 'q' to finish):\n")

    updated_metadata = {}

    # Read-only fields that should not be editable
    readonly_fields = ['error', 'PageCount', 'Duration', 'Bitrate', 'SampleRate',
                       'Format', 'Size', 'Mode', 'FileSize', 'FileName',
                       'Created', 'Accessed', 'FinderTags']

    for key, current_value in metadata.items():
        if key in readonly_fields:
            # Skip read-only fields
            updated_metadata[key] = current_value
            continue

        try:
            new_value = input(f"{key} [{current_value}]: ").strip()

            if new_value.lower() == 'q':
                print("\nCancelled.")
                return

            updated_metadata[key] = new_value if new_value else current_value
        except KeyboardInterrupt:
            print("\n\nCancelled.")
            return

    # Confirm changes
    print("\n" + "="*50)
    print("UPDATED METADATA")
    print("="*50)
    display_metadata(updated_metadata)

    confirm = input("\nSave changes? (y/n): ").strip().lower()

    if confirm == 'y':
        success, message = editor.write_metadata(updated_metadata)
        if success:
            print(f"\n✓ {message}")
        else:
            print(f"\n✗ {message}")
    else:
        print("\nChanges discarded.")


def main():
    parser = argparse.ArgumentParser(
        description='View and edit file metadata for PDFs, images, audio files, and more.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.pdf              # View and edit PDF metadata
  %(prog)s photo.jpg                 # View and edit image EXIF data
  %(prog)s song.mp3                  # View and edit audio tags
  %(prog)s --view-only document.pdf  # View metadata without editing
        """
    )

    parser.add_argument('file', help='Path to the file')
    parser.add_argument('--view-only', '-v', action='store_true',
                       help='View metadata without editing')
    parser.add_argument('--json', '-j', action='store_true',
                       help='Output metadata as JSON')

    args = parser.parse_args()

    try:
        editor = MetadataEditor(args.file)

        if args.view_only or args.json:
            metadata = editor.read_metadata()
            if args.json:
                print(json.dumps(metadata, indent=2))
            else:
                display_metadata(metadata)
        else:
            interactive_edit(editor)

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nInterrupted.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
