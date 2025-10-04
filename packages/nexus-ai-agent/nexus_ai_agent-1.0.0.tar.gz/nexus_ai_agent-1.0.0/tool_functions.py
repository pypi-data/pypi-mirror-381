"""
Tool execution functions for file operations and smart search.
"""

import os
from pathlib import Path
import fnmatch

# Common folders and patterns to exclude from searches
EXCLUDED_DIRS = {
    '.git',
    '.svn',
    '.hg',
    'node_modules',
    '__pycache__',
    '.pytest_cache',
    '.mypy_cache',
    '.tox',
    '.venv',
    'venv',
    'env',
    '.env',
    'dist',
    'build',
    '.next',
    '.nuxt',
    '.cache',
    '.parcel-cache',
    'coverage',
    '.coverage',
    'htmlcov',
    '.idea',
    '.vscode',
    '.DS_Store',
    'target',
    'bin',
    'obj',
    '.gradle',
}

def should_exclude_path(path):
    """Check if a path should be excluded based on common patterns"""
    path_parts = Path(path).parts
    # Check if any part of the path matches excluded directories
    for part in path_parts:
        if part in EXCLUDED_DIRS:
            return True
    return False


def create_file(filepath, content):
    """Create a new file with content"""
    try:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(content)
        return f"File '{filepath}' created successfully with {len(content)} characters."
    except Exception as e:
        return f"Error creating file: {str(e)}"


def read_file(filepath, start_line=None, end_line=None, max_chars=10000, 
              preview_only=False, search_term=None):
    """Read content from a file with smart reading capabilities"""
    try:
        file_path = Path(filepath)
        
        # Get file metadata
        file_size = file_path.stat().st_size
        file_size_kb = file_size / 1024
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        
        # Preview mode: return metadata and first 500 characters
        if preview_only:
            preview_content = ''.join(lines)[:500]
            if len(''.join(lines)) > 500:
                preview_content += "\n... (file continues)"
            return (
                f"📄 File Preview: '{filepath}'\n"
                f"Size: {file_size_kb:.2f} KB\n"
                f"Total Lines: {total_lines}\n\n"
                f"First 500 characters:\n{preview_content}"
            )
        
        # Search mode: return lines with search term
        if search_term:
            matched_lines = []
            search_lower = search_term.lower()
            
            for idx, line in enumerate(lines, 1):
                if search_lower in line.lower():
                    # Add context: 2 lines before and after
                    start_ctx = max(0, idx - 3)
                    end_ctx = min(len(lines), idx + 2)
                    context = lines[start_ctx:end_ctx]
                    
                    matched_lines.append({
                        'line_num': idx,
                        'content': line.rstrip(),
                        'context': ''.join(context)
                    })
            
            if not matched_lines:
                return f"No matches found for '{search_term}' in '{filepath}'"
            
            result = f"🔍 Search results for '{search_term}' in '{filepath}':\n\n"
            for match in matched_lines[:20]:  # Limit to 20 matches
                result += f"Line {match['line_num']}: {match['content']}\n"
            
            if len(matched_lines) > 20:
                result += f"\n... and {len(matched_lines) - 20} more matches"
            
            return result
        
        # Line range mode
        if start_line is not None or end_line is not None:
            start_idx = (start_line - 1) if start_line else 0
            end_idx = end_line if end_line else total_lines
            
            # Validate line numbers
            if start_idx < 0 or start_idx >= total_lines:
                return f"Error: start_line {start_line} is out of range (file has {total_lines} lines)"
            if end_idx > total_lines:
                end_idx = total_lines
            
            selected_lines = lines[start_idx:end_idx]
            content = ''.join(selected_lines)
            
            # Apply max_chars limit
            if len(content) > max_chars:
                content = content[:max_chars]
                content += f"\n\n... (truncated at {max_chars} characters)"
            
            return (
                f"📄 '{filepath}' (lines {start_idx + 1}-{end_idx}, {file_size_kb:.2f} KB total):\n\n"
                f"{content}"
            )
        
        # Full file mode with character limit
        content = ''.join(lines)
        
        # Warn if file is large
        if file_size > 50000:  # 50KB
            return (
                f"⚠️  Warning: '{filepath}' is large ({file_size_kb:.2f} KB, {total_lines} lines).\n"
                f"Consider using:\n"
                f"  - preview_only=true for a quick preview\n"
                f"  - start_line and end_line to read specific sections\n"
                f"  - search_term to find specific content\n\n"
                f"Reading first {max_chars} characters:\n\n"
                f"{content[:max_chars]}\n\n... (file continues, use line ranges to read more)"
            )
        
        # Apply max_chars limit for normal reads
        if len(content) > max_chars:
            content = content[:max_chars]
            content += f"\n\n... (truncated at {max_chars} characters, file has {total_lines} lines total)"
        
        return f"📄 Content of '{filepath}' ({file_size_kb:.2f} KB, {total_lines} lines):\n\n{content}"
        
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"


def edit_file(filepath, new_content, mode, old_content=None):
    """Edit an existing file"""
    try:
        if mode == "append":
            with open(filepath, 'a') as f:
                f.write(new_content)
            return f"Content appended to '{filepath}' successfully."
        elif mode == "replace":
            with open(filepath, 'r') as f:
                content = f.read()
            if old_content:
                content = content.replace(old_content, new_content)
            else:
                content = new_content
            with open(filepath, 'w') as f:
                f.write(content)
            return f"File '{filepath}' updated successfully."
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."
    except Exception as e:
        return f"Error editing file: {str(e)}"


def delete_file(filepath):
    """Delete a file"""
    try:
        os.remove(filepath)
        return f"File '{filepath}' deleted successfully."
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."
    except Exception as e:
        return f"Error deleting file: {str(e)}"


def list_files(directory="."):
    """List files in a directory (excludes common build/cache directories)"""
    try:
        all_items = os.listdir(directory)
        files = []
        excluded_count = 0
        
        for item in all_items:
            full_path = os.path.join(directory, item)
            if os.path.isfile(full_path):
                if not should_exclude_path(full_path):
                    files.append(item)
                else:
                    excluded_count += 1
        
        result = f"Files in '{directory}':\n" + "\n".join(f"- {f}" for f in sorted(files))
        
        if excluded_count > 0:
            result += f"\n\n(Excluded {excluded_count} files from system/build directories)"
        
        return result
    except Exception as e:
        return f"Error listing files: {str(e)}"


def smart_search(directory=".", filename_pattern=None, content_query=None, 
                recursive=True, file_extensions=None):
    """
    Intelligent search for files by name pattern and/or content.
    Returns detailed results with file paths, matched lines, and context.
    """
    try:
        if not filename_pattern and not content_query:
            return "Error: Please provide either a filename pattern or content to search for."
        
        results = {
            "matched_files": [],
            "content_matches": [],
            "summary": {}
        }
        
        search_path = Path(directory)
        if not search_path.exists():
            return f"Error: Directory '{directory}' does not exist."
        
        # Get all files to search
        if recursive:
            all_files = [f for f in search_path.rglob("*") if f.is_file() and not should_exclude_path(f)]
        else:
            all_files = [f for f in search_path.glob("*") if f.is_file() and not should_exclude_path(f)]
        
        # Filter by file extensions if provided
        if file_extensions:
            extensions = [ext.lower().lstrip('.') for ext in file_extensions]
            all_files = [f for f in all_files if f.suffix.lstrip('.').lower() in extensions]
        
        # Search by filename pattern
        if filename_pattern:
            for file_path in all_files:
                if fnmatch.fnmatch(file_path.name, filename_pattern):
                    results["matched_files"].append({
                        "path": str(file_path),
                        "name": file_path.name,
                        "size": file_path.stat().st_size
                    })
        
        # Search by content
        if content_query:
            query_lower = content_query.lower()
            
            for file_path in all_files:
                try:
                    # Skip binary files
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                    
                    matched_lines = []
                    for line_num, line in enumerate(lines, 1):
                        if query_lower in line.lower():
                            # Add context (line before and after if available)
                            context_start = max(0, line_num - 2)
                            context_end = min(len(lines), line_num + 1)
                            context = lines[context_start:context_end]
                            
                            matched_lines.append({
                                "line_number": line_num,
                                "line": line.strip(),
                                "context": [l.strip() for l in context]
                            })
                    
                    if matched_lines:
                        results["content_matches"].append({
                            "path": str(file_path),
                            "name": file_path.name,
                            "matches": matched_lines[:5]  # Limit to 5 matches per file
                        })
                
                except (PermissionError, UnicodeDecodeError):
                    continue
        
        # Build summary
        results["summary"] = {
            "files_matched_by_name": len(results["matched_files"]),
            "files_with_content_matches": len(results["content_matches"]),
            "search_directory": directory,
            "recursive": recursive
        }
        
        # Format output
        output = []
        output.append(f"🔍 Smart Search Results")
        output.append(f"{'='*60}")
        output.append(f"Directory: {directory} (Recursive: {recursive})")
        output.append(f"ℹ️  Excluding: .git, node_modules, __pycache__, and other build/cache directories")
        
        if filename_pattern:
            output.append(f"Filename Pattern: {filename_pattern}")
        if content_query:
            output.append(f"Content Query: '{content_query}'")
        if file_extensions:
            output.append(f"File Extensions: {', '.join(file_extensions)}")
        
        output.append(f"\n📊 Summary:")
        output.append(f"  - Files searched: {len(all_files)}")
        output.append(f"  - Files matched by name: {results['summary']['files_matched_by_name']}")
        output.append(f"  - Files with content matches: {results['summary']['files_with_content_matches']}")
        
        # Show filename matches
        if results["matched_files"]:
            output.append(f"\n📁 Files Matching Pattern:")
            for match in results["matched_files"][:10]:  # Limit to 10
                size_kb = match['size'] / 1024
                output.append(f"  • {match['path']} ({size_kb:.2f} KB)")
        
        # Show content matches
        if results["content_matches"]:
            output.append(f"\n📝 Content Matches:")
            for file_match in results["content_matches"][:5]:  # Limit to 5 files
                output.append(f"\n  📄 {file_match['path']}")
                for match in file_match['matches'][:3]:  # Limit to 3 matches per file
                    output.append(f"     Line {match['line_number']}: {match['line'][:100]}")
        
        if not results["matched_files"] and not results["content_matches"]:
            output.append(f"\n❌ No matches found.")
        
        return "\n".join(output)
    
    except Exception as e:
        return f"Error during search: {str(e)}"


# Map tool names to functions
tool_functions = {
    "create_file": create_file,
    "read_file": read_file,
    "edit_file": edit_file,
    "delete_file": delete_file,
    "list_files": list_files,
    "smart_search": smart_search
}
