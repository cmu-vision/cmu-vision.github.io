#!/bin/bash
# Run after merging PRs: pull, regenerate HTML, commit, push
set -e
cd "$(dirname "$0")"
echo "Pulling latest from origin/main..."
git pull origin main
echo "Regenerating site..."
python3 generate.py
echo "Committing generated files..."
git add index.html people.html research.html courses.html papers.html
git status
if git diff --cached --quiet; then
  echo "No generated changes to commit."
else
  git commit -m "Regenerate site after merging PRs"
  echo "Pushing to origin/main..."
  git push origin main
  echo "Done. Site will update after GitHub Pages builds."
fi
