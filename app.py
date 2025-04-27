<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>My Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: white;
            padding: 15px 0;
            text-align: center;
        }
        nav {
            background-color: #444;
            overflow: hidden;
        }
        nav a {
            float: left;
            display: block;
            color: white;
            padding: 14px 16px;
            text-align: center;
            text-decoration: none;
        }
        nav a:hover {
            background-color: #ddd;
            color: black;
        }
        section {
            padding: 20px;
            margin: 20px;
            background-color: white;
            border-radius: 8px;
        }
        h1, h2 {
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .row {
            display: flex;
            justify-content: space-between;
        }
        .column {
            flex: 1;
            padding: 10px;
        }
        .skills {
            display: flex;
            flex-wrap: wrap;
        }
        .skills div {
            margin-right: 15px;
            background-color: #ddd;
            padding: 5px 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
        }
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        .contact-form button {
            background-color: #333;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .contact-form button:hover {
            background-color: #555;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
    </style>
</head>
<body>

<header>
    <h1>Welcome to My Portfolio</h1>
    <p>Your one-stop destination for all my projects and experience!</p>
</header>

<nav>
    <a href="#about">About Me</a>
    <a href="#projects">Projects</a>
    <a href="#skills">Skills</a>
    <a href="#contact">Contact</a>
</nav>

<section id="about">
    <div class="container">
        <h2>About Me</h2>
        <p>Hello, I'm John Doe, a passionate web developer with a love for creating innovative solutions. With over 5 years of experience, I've worked on various projects ranging from simple static websites to complex web applications. I specialize in front-end development and enjoy creating visually stunning designs that provide a smooth user experience.</p>
        <p>In my free time, I love to learn about new technologies, read tech blogs, and contribute to open-source projects. My goal is to continually improve my skills and stay updated with the latest web development trends.</p>
    </div>
</section>

<section id="projects">
    <div class="container">
        <h2>My Projects</h2>
        <div class="row">
            <div class="column">
                <h3>Project One</h3>
                <p>This is a responsive website built with HTML, CSS, and JavaScript. It features a clean and modern design, with a focus on user experience. The website is fully responsive, adapting to different screen sizes.</p>
                <p>Technologies Used: HTML, CSS, JavaScript</p>
            </div>
            <div class="column">
                <h3>Project Two</h3>
                <p>This project is a web application built using React.js and Node.js. It allows users to create and manage tasks efficiently with real-time updates and notifications. The backend is powered by Node.js, and the app is hosted on AWS.</p>
                <p>Technologies Used: React.js, Node.js, AWS</p>
            </div>
        </div>
        <div class="row">
            <div class="column">
                <h3>Project Three</h3>
                <p>This is an e-commerce website that allows users to browse and purchase products. It includes a secure checkout system and integrates with a payment gateway for smooth transactions.</p>
                <p>Technologies Used: HTML, CSS, JavaScript, Stripe API</p>
            </div>
            <div class="column">
                <h3>Project Four</h3>
                <p>This project is a content management system (CMS) built using PHP and MySQL. It allows users to create, edit, and manage their website content with ease. The CMS is designed to be user-friendly and secure.</p>
                <p>Technologies Used: PHP, MySQL</p>
            </div>
        </div>
    </div>
</section>

<section id="skills">
    <div class="container">
        <h2>My Skills</h2>
        <p>Here are some of the skills I have gained over the years:</p>
        <div class="skills">
            <div>HTML5</div>
            <div>CSS3</div>
            <div>JavaScript</div>
            <div>React.js</div>
            <div>Node.js</div>
            <div>PHP</div>
            <div>MySQL</div>
            <div>Git</div>
        </div>
    </div>
</section>

<section id="contact">
    <div class="container">
        <h2>Contact Me</h2>
        <p>If you would like to get in touch, feel free to use the contact form below. I would love to hear from you!</p>
        <form class="contact-form">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" rows="5" placeholder="Your Message" required></textarea>
            <button type="submit">Send Message</button>
        </form>
        <h3>Or reach me at:</h3>
        <ul>
            <li>Email: johndoe@example.com</li>
            <li>Phone: +1 (555) 123-4567</li>
        </ul>
    </div>
</section>

<section id="experience">
    <div class="container">
        <h2>Work Experience</h2>
        <table>
            <thead>
                <tr>
                    <th>Job Title</th>
                    <th>Company</th>
                    <th>Year</th>
                    <th>Location</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Front-End Developer</td>
                    <td>Tech Corp</td>
                    <td>2020-Present</td>
                    <td>New York, NY</td>
                </tr>
                <tr>
                    <td>Web Developer</td>
                    <td>Web Solutions</td>
                    <td>2018-2020</td>
                    <td>Los Angeles, CA</td>
                </tr>
                <tr>
                    <td>Junior Developer</td>
                    <td>CodeWorks</td>
                    <td>2016-2018</td>
                    <td>San Francisco, CA</td>
                </tr>
            </tbody>
        </table>
    </div>
</section>

<footer>
    <p>© 2025 John Doe. All rights reserved.</p>
</footer>

</body>
</html>
