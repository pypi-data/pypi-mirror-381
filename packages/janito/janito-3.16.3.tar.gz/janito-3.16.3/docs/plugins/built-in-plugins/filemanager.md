# File Manager Plugin

## Overview

The File Manager plugin provides essential file and directory operations for managing project files. This plugin enables basic file system operations that are crucial for code editing and project management.

## Resources Provided

### Tools

| Tool Name | Function | Description |
|-----------|----------|-------------|
| `create_file` | Create new files with content | Creates a new file at the specified path with optional content and overwrite capability |
| `read_files` | Read multiple files at once | Reads the contents of multiple files and returns them as a concatenated string |
| `view_file` | Read specific portions of files | Reads specific lines or the entire content of a file with optional line range |
| `replace_text_in_file` | Find and replace text in files | Searches for exact text in a file and replaces it with new text (single or all occurrences) |
| `validate_file_syntax` | Check file syntax | Validates the syntax of various file types (Python, Markdown, JSON, etc.) |
| `create_directory` | Create new directories | Creates a new directory at the specified path. If the directory already exists, provides a summary of its contents including file/subdirectory counts and examples |
| `remove_directory` | Remove directories | Deletes directories, with optional recursive removal of non-empty directories |
| `remove_file` | Delete files | Removes a file at the specified path |
| `copy_file` | Copy files or directories | Copies one or more files/directories to a target location |
| `move_file` | Move or rename files/directories | Moves or renames files and directories |
| `find_files` | Search for files by pattern | Finds files matching a pattern in specified directories, respecting .gitignore |

## Usage Examples

### Creating a New File

The `create_file` tool provides comprehensive file creation with built-in safety features and automatic validation.

**Basic Usage:**
```json
{
  "tool": "create_file",
  "path": "src/hello.py",
  "content": "print('Hello, World!')"
}
```

**Advanced Examples:**

Create nested directory structure:
```json
{
  "tool": "create_file",
  "path": "src/components/Button/index.js",
  "content": "export default function Button() { return <button>Click me</button>; }"
}
```

Create configuration file with environment variables:
```json
{
  "tool": "create_file",
  "path": "$HOME/.myapp/config.json",
  "content": "{\n  \"api_url\": \"https://api.example.com\",\n  \"timeout\": 30\n}"
}
```

Overwrite existing file (use with caution):
```json
{
  "tool": "create_file",
  "path": "README.md",
  "content": "# My Project\n\nUpdated documentation...",
  "overwrite": true
}
```

**Safety Features:**

- **Overwrite Protection**: Prevents accidental file overwrites by default
- **Syntax Validation**: Automatically checks Python, JavaScript, JSON, YAML, and other common file types
- **Path Expansion**: Supports `~` for home directory and environment variables like `$HOME`
- **Directory Creation**: Automatically creates parent directories as needed
- **Encoding Safety**: Uses UTF-8 encoding with proper error handling for international characters
- **Loop Protection**: Prevents excessive file creation calls (max 5 per 10 seconds per file)

**Return Values:**

- Success: Includes line count and syntax validation results
- Failure: Provides detailed error messages and existing content preview when overwrite is blocked
- Validation: Shows syntax check results for supported file types

### Reading Multiple Files
```json
{
  "tool": "read_files",
  "paths": ["src/main.py", "src/utils.py"]
}
```

### Finding Python Files
```json
{
  "tool": "find_files",
  "paths": ".",
  "pattern": "*.py"
}
```

### Creating a New Directory

The `create_directory` tool creates new directories with enhanced feedback when directories already exist.

**Basic Usage:**
```json
{
  "tool": "create_directory",
  "path": "src/components"
}
```

**Enhanced Feedback for Existing Directories:**
When attempting to create a directory that already exists, the tool now provides a detailed summary of the directory's contents:

```
❗ Cannot create directory: 'src/components' already exists.
Contains: 3 files, 2 subdirectories.
Examples: 📄 index.js, 📄 styles.css, 📁 utils (and 2 more)
```

**Content Summary Features:**

- **File and Directory Counts**: Shows the total number of files and subdirectories
- **Content Examples**: Displays up to 3 items (sorted alphabetically) with visual indicators:
  - 📁 for directories
  - 📄 for files
- **Overflow Indicator**: Mentions if there are more items than shown
- **Empty Directory Handling**: Clearly indicates when a directory is empty
- **Error Handling**: Gracefully handles permission issues or other access problems

This enhancement helps users quickly understand what's already in an existing directory without needing to run additional commands.

## Configuration

This plugin does not require any specific configuration and uses the system's default file permissions and access controls.

## Security Considerations

- File operations are subject to the user's file system permissions
- Path validation prevents directory traversal attacks
- Sensitive file operations require explicit user confirmation in interactive mode

## Integration

The File Manager plugin integrates with the core Janito system to provide file operations that can be used in automation scripts, code generation workflows, and project management tasks.

## Configuration

This plugin does not require any specific configuration and uses the system's default file permissions and access controls.

## Security Considerations

- File operations are subject to the user's file system permissions
- Path validation prevents directory traversal attacks
- Sensitive file operations require explicit user confirmation in interactive mode

## Integration

The File Manager plugin integrates with the core Janito system to provide file operations that can be used in automation scripts, code generation workflows, and project management tasks.