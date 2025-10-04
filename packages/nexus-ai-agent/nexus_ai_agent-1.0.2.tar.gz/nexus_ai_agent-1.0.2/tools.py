# Tool definitions for the Anthropic API agent

tools = [
    {
        "name": "create_file",
        "description": "Creates a new file with the specified content. If the file already exists, it will be overwritten.",
        "input_schema": {
            "type": "object",
            "properties": {
                "filepath": {
                    "type": "string",
                    "description": "The path where the file should be created (e.g., 'documents/note.txt')"
                },
                "content": {
                    "type": "string",
                    "description": "The content to write to the file"
                }
            },
            "required": ["filepath", "content"]
        }
    },
    {
        "name": "read_file",
        "description": "Reads and returns the content of an existing file. Supports smart reading with line ranges, character limits, and preview mode to avoid reading huge files.",
        "input_schema": {
            "type": "object",
            "properties": {
                "filepath": {
                    "type": "string",
                    "description": "The path of the file to read"
                },
                "start_line": {
                    "type": "integer",
                    "description": "Starting line number to read from (1-indexed). If not provided, reads from the beginning."
                },
                "end_line": {
                    "type": "integer",
                    "description": "Ending line number to read to (1-indexed, inclusive). If not provided, reads to the end or max_chars limit."
                },
                "max_chars": {
                    "type": "integer",
                    "description": "Maximum number of characters to return (default: 10000). Prevents token explosion from huge files."
                },
                "preview_only": {
                    "type": "boolean",
                    "description": "If true, returns only file metadata and first 500 characters as a preview (default: false)"
                },
                "search_term": {
                    "type": "string",
                    "description": "If provided, returns only lines containing this search term with context lines around matches."
                }
            },
            "required": ["filepath"]
        }
    },
    {
        "name": "edit_file",
        "description": "Edits an existing file by replacing old content with new content, or appending to the file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "filepath": {
                    "type": "string",
                    "description": "The path of the file to edit"
                },
                "old_content": {
                    "type": "string",
                    "description": "The content to replace (if doing a replacement). Leave empty to append."
                },
                "new_content": {
                    "type": "string",
                    "description": "The new content to insert"
                },
                "mode": {
                    "type": "string",
                    "enum": ["replace", "append"],
                    "description": "Whether to replace old content or append to the end of the file"
                }
            },
            "required": ["filepath", "new_content", "mode"]
        }
    },
    {
        "name": "delete_file",
        "description": "Deletes a file from the filesystem.",
        "input_schema": {
            "type": "object",
            "properties": {
                "filepath": {
                    "type": "string",
                    "description": "The path of the file to delete"
                }
            },
            "required": ["filepath"]
        }
    },
    {
        "name": "list_files",
        "description": "Lists all files in a specified directory. Automatically excludes common build/cache directories like .git, node_modules, __pycache__, etc.",
        "input_schema": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "The directory path to list files from (defaults to current directory)"
                }
            },
            "required": []
        }
    },
    {
        "name": "smart_search",
        "description": "Performs an intelligent search across files in a directory. Can search by filename pattern, file content, or both. Supports recursive search through subdirectories. Automatically excludes irrelevant directories (.git, node_modules, __pycache__, build, dist, etc.).",
        "input_schema": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "The directory to search in (defaults to current directory)"
                },
                "filename_pattern": {
                    "type": "string",
                    "description": "Pattern to match filenames (e.g., '*.txt', 'test*', 'config.json'). Supports wildcards."
                },
                "content_query": {
                    "type": "string",
                    "description": "Text to search for within file contents. Case-insensitive search."
                },
                "recursive": {
                    "type": "boolean",
                    "description": "Whether to search subdirectories recursively (default: true)"
                },
                "file_extensions": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Filter by file extensions (e.g., ['txt', 'py', 'json'])"
                }
            },
            "required": []
        }
    }
]
