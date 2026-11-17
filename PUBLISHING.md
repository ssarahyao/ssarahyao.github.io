# How to publish your site

Your site will live at **https://ssarahyao.github.io**. It's free, and you only set it up once.

## 1. Create the repository
1. Sign in to github.com as **ssarahyao**.
2. Click **+ → New repository**.
3. Name it exactly `ssarahyao.github.io`, make it **Public**, and don't add a README.
4. Click **Create repository**.

## 2. Upload the site
Open Terminal and paste these one at a time:

```bash
cd ~/Downloads/recruting/website
```

```bash
git init -b main && git add . && git commit -m "Launch portfolio site"
```

```bash
git remote add origin https://github.com/ssarahyao/ssarahyao.github.io.git && git push -u origin main
```

> Use Terminal (or GitHub Desktop) rather than dragging files onto github.com.
> The drag-and-drop uploader skips the hidden `.github` folder, which runs
> the Stanford Daily auto-update.

## 3. Turn on GitHub Pages
1. In the repo, go to **Settings → Pages**.
2. Under **Source**, pick **Deploy from a branch**, then branch `main`, folder `/ (root)`. Click **Save**.
3. Wait about a minute, then open https://ssarahyao.github.io.

## 4. Check the Stanford Daily auto-update
- Go to the repo's **Actions** tab → **Update Stanford Daily articles** → **Run workflow** to test it once.
- After that it runs every morning on its own. When you publish a new Daily article, it shows up on your site within a day.
- If the run fails with a permissions error, go to **Settings → Actions → General → Workflow permissions** and choose **Read and write permissions**.
- GitHub pauses scheduled jobs on repos with no activity for 60 days. If that happens, the Actions tab shows a button to turn it back on.

## Updating the site later
Edit the files, then run:

```bash
cd ~/Downloads/recruting/website && git pull && git add . && git commit -m "Update site" && git push
```

Run `git pull` first because the auto-updater may have added commits of its own.

## Optional: a custom domain
You can buy a domain like `sarahyao.com` (about $12 a year), then add it under **Settings → Pages → Custom domain**.
