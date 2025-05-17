@echo off
cd /d %~dp0

echo 🧠 Checking for updates from GitHub...
git pull --rebase

echo 🌍 Running Storyworld Script...
python init_storyworld.py

echo 🌀 Staging files...
git add .

echo 📝 Committing...
git commit -m "Auto update from storyworld script"

echo 🚀 Pushing to GitHub...
git push origin main

echo ✅ Done! Press any key to close...
pause >nul
