# Official Starter Template for Om StartUp Framework

# Getting Started

:::info Prerequisites

- Requires [Python](https://www.python.org/) (>=3.x)
- Requires [Node.js](https://nodejs.org/)

:::


## Installation

Clone Starter Template

```bash
git clone https://github.com/omkarcloud/om-startup-framework my-om-project
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
