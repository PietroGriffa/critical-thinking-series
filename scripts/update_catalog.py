#!/usr/bin/env python3
"""
Script to auto-generate the topics catalog in README.md
"""

import re
import yaml
from pathlib import Path

def load_topic_metadata(topic_path):
    """Load metadata from topic.yaml file"""
    yaml_path = topic_path / "topic.yaml"
    if yaml_path.exists():
        with open(yaml_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return None

def generate_catalog_table():
    """Generate the markdown table for the topics catalog"""
    topics_dir = Path("topics")
    topics = []
    
    # Find all topic directories
    for topic_dir in sorted(topics_dir.iterdir()):
        digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        if topic_dir.is_dir() and topic_dir.name.startswith(digits):
            metadata = load_topic_metadata(topic_dir)
            if metadata:
                topics.append({
                    'path': topic_dir,
                    'metadata': metadata
                })
    
    # Sort by topic number
    topics.sort(key=lambda x: x['metadata'].get('number', 0))
    
    # Generate table
    table_lines = [
        "| # | Topic |",
        "|---|-------|"
    ]
    
    for topic in topics:
        meta = topic['metadata']
        number = meta.get('number', '?')
        title = meta.get('title', 'Unknown')
        path = topic['path'].name
        
        # Create table row
        row = f"| {number} | [{title}](topics/{path}) |"
        table_lines.append(row)
    
    return "\n".join(table_lines)

def update_readme():
    """Update the README.md file with the new catalog"""
    readme_path = Path("README.md")
    
    if not readme_path.exists():
        print("README.md not found")
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate new catalog
    new_catalog = generate_catalog_table()
    
    # Replace the catalog section
    pattern = (
        r'<!-- BEGIN AUTO-GENERATED CATALOG -->.*?'
        r'<!-- END AUTO-GENERATED CATALOG -->'
    )
    replacement = (
        f"<!-- BEGIN AUTO-GENERATED CATALOG -->\n"
        f"{new_catalog}\n"
        f"<!-- END AUTO-GENERATED CATALOG -->"
    )
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write back to file
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("README.md catalog updated successfully")

if __name__ == "__main__":
    update_readme()