# Mohammed Ali's Personal Portfolio Website

This is my final project for CS50, my first computer science course. I built a personal portfolio website using Flask, Python, CSS, HTML and JavaScript to showcase my skills, projects, and achievements as a web developer.

You can watch a video presentation of my project [HERE](https://www.youtube.com/watch?v=QDCi17eFgSg).

## Features and some challenges

- There is the Homepage with my name, animated picture, bio. This part was at first very challenging since I did not know what I wanted the page to look like, and given the nearly infinite possibilities I was overwhelmed. So, I developed a plan, where I looked up the most popular and efficient way to design a personal portfolio site. The Website is the result.
- A skills section with the technologies and tools that I used for creating the site, I had the idea of creating my own slideshow first, and then realised that it can be made even prettier by using third party libraries. I used Swiper.js for the design of my slides, and I am very satisfied with the result.
- A responsive design that adapts to different screen sizes and devices. The responsiveness did not cause me a major headache since bootstrap took care of the bulk of the work for me.
- The homepage design was based on a video from a youtuber by the name of [Kevin Powell]{https://www.youtube.com/@KevinPowell}, I really liked the svg trick used to make the pattern, and the skewed background. I also used the changing colours animation that's behind the cat image.
- Javascript script.js was meant to have only three lines of code initially but later I changed the design since I figured having my html and js in the same file was not the best option. I compartmentalised my js code to be specifically loaded to each page depending on the url of the page.
- I made major flaws in my python code earlier in the project, since I decided to implement a forget password functionality but later caused my entire page to bug out, since handling more than one submit button in the same page seems to cause some unexpected difficulties for flask.
- I implemented an automatic email sender, which I am really proud of, and learned how to store my os variable securely in multiple ways.
- The decision to develop locally has been hard, since I am not used to downloading the packages and creating my own environment for development. It has cost me a lot of time to get used to it and set up my VS code environment the way I wanted it to be.
- Personally, the most difficult part about this project was not the code nor the effort, it was that it depended entirely on me, and I had no right or wrong way of doing it. I got through eventually which really made me more excited about the future possibility of learning further.

## Technologies

- Flask: a micro web framework for Python that handles routing, templating, and server-side logic
- Python: a high-level programming language that handles data processing and backend logic
- CSS: a style sheet language that defines the appearance and layout of the website
- HTML: a markup language that defines the structure and content of the website
- JavaScript: a scripting language that enables dynamic and interactive features on the website

## How to run

To run this project locally, you need to have Python 3 and Flask installed on your machine. You can follow these steps:

- Install the required packages using `pip install -r requirements.txt`
- Set the FLASK_APP environment variable to app.py using `export FLASK_APP=app.py` (Linux/Mac) or `set FLASK_APP=app.py` (Windows)
- Run the Flask server using `flask run`
- Open your browser and go to http://localhost:5000 to view the website
