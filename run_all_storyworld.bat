@echo off
cd /d %~dp0

echo 🧠 Pulling latest from GitHub...
git pull --rebase

echo 🌍 Running storyworld builder...

python init_storyworld.py

echo 🌀 Staging files...
git add .

echo 📝 Committing...
git commit -m "Auto update from storyworld script"

echo 🚀 Pushing to GitHub...
git push origin main

echo 🌐 Launching Streamlit app in browser...
start "" streamlit run storyworld_app.py

echo ✅ All done! Streamlit is now running in your browser.
pause
