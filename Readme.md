# Todo App Using Flask-py
A Todo app Developed using Flask-py, Designed in Tailwind-css.

Development Database used **Sqlite3**\
Deployement Database used **PostgreSQL**

# Available Scripts
In the project directory, you can run:

python app.py

Runs the app in the development mode.\
Open http://localhost:3000 to view it in the browser.

## Tailwind Setup (Not Including app.py)
- npm init -y
- npm install -D tailwindcss postcss autoprefixer vite
- npx tailwindcss init -p
- In package.json change\
	"scripts": {\
    "start": "vite",\
    "watch-css": "npx tailwindcss -i ./static/css/src/input.css -o ./static/css/dist/output.css --watch"\
  },
- In tailwind.config.js change content: {"./templates/**/*.{html,htm}"}
- Create input.css and add\
	@tailwind base;\
	@tailwind components;\
	@tailwind utilities;
- To start server : npm run start

# Learn More
To Learn [Python](https://www.python.org/doc/)\
To Learn [Flask](https://flask.palletsprojects.com/en/2.2.x/)\
To Learn [Tailwind](https://tailwindcss.com/docs/installation)\
Flask, Html & Css [Integration](https://jinja.palletsprojects.com/en/3.1.x/)\
Deployment Done On [Render](https://render.com)

