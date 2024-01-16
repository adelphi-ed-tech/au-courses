#!/bin/bash

# Directory containing Markdown files
DIRECTORY="."

# Loop over all Markdown files in the specified directory
for file in "$DIRECTORY"/*.md; do
    # Read the title and author from the Pandoc headers
    read -r TITLE_LINE < "$file"
    read -r AUTHOR_LINE <&3

    # Extract title and author, removing the '%' character
    TITLE=${TITLE_LINE#\% }
    AUTHOR=${AUTHOR_LINE#\% }

    # Create Jekyll front matter
    FRONT_MATTER="---\nlayout: syllabus\ntitle: \"$TITLE\"\nauthor: \"$AUTHOR\"\n---\n"

    # Add front matter to the file
    (echo -e "$FRONT_MATTER" && cat "$file") > temp && mv temp "$file"
done
