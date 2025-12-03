# Pair Extraordinaire Badge Guide 👥

## What you need: Co-author a commit that gets merged into a pull request

### Quick Method (5 minutes):

**Step 1: Create a commit with co-authors**
```bash
git checkout -b pair-feature
echo "Pair programming work" >> test.txt
git add test.txt
git commit -m "Add pair programming feature

Co-authored-by: Friend Name <friend@users.noreply.github.com>
Co-authored-by: Another Friend <another@users.noreply.github.com>"
```

**Step 2: Push and create PR**
```bash
git push origin pair-feature
```

**Step 3: Go to GitHub**
1. Create a pull request from `pair-feature` branch
2. Merge the pull request

✅ **Done!** Badge appears for everyone who was co-authored.

---

## Important Notes:
- Need at least 1 co-author (2+ people total)
- Use format: `Co-authored-by: Name <email@example.com>`
- Blank line before co-author lines
- Each person needs their GitHub-verified email
- Find GitHub email: `username@users.noreply.github.com`

---

## Alternative: GitHub Web Interface

1. Edit a file on GitHub
2. In commit message box, add:
```
Your commit message

Co-authored-by: Friend <friend@users.noreply.github.com>
```
3. Create new branch and PR
4. Merge the PR

✅ **Both you and your co-author get the badge!**
