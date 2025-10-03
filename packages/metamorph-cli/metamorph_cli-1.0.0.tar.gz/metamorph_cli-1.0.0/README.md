# MetaMorph

Transform your file metadata with ease. A cross-platform Python CLI tool to view and edit metadata for various file types including PDFs, images, audio files, and general file attributes.

## Features

- **PDF Files**: Edit metadata like Title, Author, Subject, Creator, Producer, etc.
- **Image Files**: View EXIF data (JPG, PNG, TIFF, BMP, GIF)
- **Audio Files**: Edit tags for MP3, MP4, M4A, FLAC, OGG, WAV
- **General Files**: Modify timestamps and permissions
- **macOS Extended Attributes**: View and edit "Where from" URLs, Finder comments, and view Finder tags

## Installation

### Option 1: Install via pip (Recommended)

```bash
pip install metamorph-cli
```

After installation, you can use it anywhere:
```bash
metamorph yourfile.pdf
```

### Option 2: Install from source

```bash
git clone https://github.com/yourusername/metamorph.git
cd metamorph
./install.sh
```

### Option 3: Run locally (Development)

```bash
git clone https://github.com/yourusername/metamorph.git
cd metamorph
pip install -r requirements.txt
./mm yourfile.pdf
```

## Usage

### Interactive Mode (Edit Metadata)

```bash
metamorph document.pdf
```

This will:
1. Display all current metadata
2. Prompt you to edit each field
3. Ask for confirmation before saving

### View-Only Mode

```bash
metamorph --view-only document.pdf
metamorph -v photo.jpg
```

### JSON Output

```bash
metamorph --json song.mp3
```

## Examples

### Edit PDF metadata
```bash
metamorph invoice.pdf
```

### View image EXIF data
```bash
metamorph --view-only vacation.jpg
```

### Edit audio tags
```bash
metamorph song.mp3
```

### View file attributes as JSON
```bash
metamorph --json document.txt
```

## Supported File Types

- **PDF**: .pdf
- **Images**: .jpg, .jpeg, .png, .tiff, .bmp, .gif
- **Audio**: .mp3, .mp4, .m4a, .flac, .ogg, .wav
- **General**: Any file (for basic attributes)

## How It Works

The tool automatically detects the file type and uses the appropriate library:
- **PyPDF2** for PDF files
- **Pillow** for image EXIF data
- **Mutagen** for audio file tags
- **os/pathlib** for general file attributes
- **xattr** (macOS) for extended attributes like "Where from" and Finder comments

## Metadata Types

### macOS Extended Attributes
On macOS, MetaMorph can read and edit special Finder metadata:
- **WhereFrom**: The URL where a file was downloaded from
- **FinderComment**: Comments visible in Finder's Get Info panel
- **FinderTags**: View color tags (read-only)

### PDF Metadata
Standard PDF fields like Title, Author, Subject, Keywords, Creator, Producer, etc.

### Image EXIF
View EXIF data including camera settings, GPS coordinates, timestamps (editing limited)

### Audio Tags
Common ID3 tags: title, artist, album, date, genre, track number, etc.

## Notes

- Image EXIF editing is limited (view-only for most fields)
- Some metadata fields are read-only (e.g., file size, page count, Finder tags)
- macOS extended attributes require macOS (uses `xattr` command)
- Always backup important files before editing metadata
- Press `Ctrl+C` or type 'q' to cancel editing at any time

## License

MIT
