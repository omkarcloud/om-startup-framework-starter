<p align="center">
  <img src="https://www.omkar.cloud/images/favicon/prod/favicon-256x256.png" alt="omkar" />
</p>
  <div align="center" style="margin-top: 0;">
  <h1>✨ Official Starter Template for Om StartUp Framework ✨</h1>
  <!-- <p>💦 Enjoy the Rain of Google Maps Leads 💦</p> -->
</div>
<em>
  <h5 align="center">(Programming Language - Python 3)</h5>
</em>
<p align="center">
  <a href="#">
    <img alt="om-startup-framework-starter forks" src="https://img.shields.io/github/forks/omkarcloud/om-startup-framework-starter?style=for-the-badge" />
  </a>
  <a href="#">
    <img alt="Repo stars" src="https://img.shields.io/github/stars/omkarcloud/om-startup-framework-starter?style=for-the-badge&color=yellow" />
  </a>
  <a href="#">
    <img alt="om-startup-framework-starter License" src="https://img.shields.io/github/license/omkarcloud/om-startup-framework-starter?color=orange&style=for-the-badge" />
  </a>
  <a href="https://github.com/omkarcloud/om-startup-framework-starter/issues">
    <img alt="issues" src="https://img.shields.io/github/issues/omkarcloud/om-startup-framework-starter?color=purple&style=for-the-badge" />
  </a>
</p>
<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/om-startup-framework-starter.svg" width="80px" height="28px" alt="View" />
</p>

---


## Getting Started

:::info Prerequisites

- Requires [Python](https://www.python.org/) (>=3.x)
- Requires [Node.js](https://nodejs.org/)

:::


## Installation

Clone Starter Template

```bash
git clone https://github.com/omkarcloud/om-startup-framework-starter my-om-project
cd my-om-project
```

Then change into frontend/ directory and install dependencies.

```bash
cd frontend/
npm install --legacy-peer-deps
```

Then change into blog/ directory and install dependencies.

```bash
cd blog/
npm install
```

Then change into backend/ directory, install dependencies, migrate database and seed with data.

```bash
cd backend/
python -m pip install -r requirements.txt
npm run db:delete-and-seed
```

## Run the Frontend and Backend Server

Start the frontend server

```bash
cd frontend/
npm run dev
```

In a seperate terminal start the backend server

```bash
cd backend/
npm run dev
```

Now, visit ![http://localhost:3000](http://localhost:3000) to see the home page with a nav bar linking to various pages of application. Explore the pages by clicking on navigation links to get a big picture of feautres of your application.

![](https://www.omkar.cloud/om-startup-framework/assets/images/getting_started_server_starter-05e25c7e881441d4c02776beb920e56e.png)

## Run the Blog Server

Most of your time will be spent writing frontend and backend code. Occasionally, you will need to run the blog server to preview the articles you write. Run following Command to spin up the blog server 

```bash
cd blog/
npm run dev
```

Now visit ![http://localhost:4000/blog/](http://localhost:4000/blog/) to see the blog home page.

![](https://www.omkar.cloud/om-startup-framework/assets/images/getting_started_blog_starter-487dc220eee2e89bfc3afacffe353d06.png)

For more information read Om StartUp Framework Documentation at [https://www.omkar.cloud/om-startup-framework/](https://www.omkar.cloud/om-startup-framework/) 
---

🙏 Made in Bharat 🇮🇳. Vande Mataram 🙏
