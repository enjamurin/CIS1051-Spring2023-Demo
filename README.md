# READ ME: Documentation and Set-up Instructions

CloSets: Wardrobe Organizer

Video URL: https://www.youtube.com/watch?v=06jY-6IEMtA

Group Members:
Taznuba Hossain and Nitya Enjamuri

## Goal

The goal is to create an online clothing management tool. Each user will be able to log in and log out, and access the rest of the functionality within their account.

## Definitions
**Item** > a piece of clothing uploaded by the user. Object containing an image, and descriptors: type, color, style, season, fit. 
Ex: shirt

**Outfit** > user generated collection of items that are grouped together as one object. Ex: shirt, pants, shoes etc.

**Closet** > a folder that contains both items and outfits. Subclosets are user generated, while My Closet is automatically created for each user.

**My Closet** > automatically generated folder that contains every single item of clothing added by the user.

**Subclosets** > user generated "closets" that they can rename. In these closets, users can designate certain items of clothing or outfits.
The same items can be found in multiple closets.
Ex: Closet named "Hawaii Trip" includes swimsuit, flipflops and white shirt, while "Dinner Fits" would include a blazer and the same white shirt.

## Structure
Front end: HTML, CSS, Javascript

Backend: Flask framework utilizing SQLAlchemy to access SQLite database

## Download and Install the Following
- Git Bash: include pip and add to Path
    - Set up connection with Github
    - Create/register SSH keys if needed 
- Code editor: ex. VSCode
- Python:
    - Python packages: 
        - py -m pip install flask
        - py -m pip install flask-login
        - py -m pip install flask-sqlalchemy
        
## Challenges Faced
Creating the login/signup feature for our website was definitely one of the biggest challenges we faced. We especially had difficultly figuring out how to store all the data for later use, where we could allow users to create accounts, log in, store their clothing items, and then logout. It was a learning curve, and we spent extra time researching and testing different approaches to make it work seamlessly. We tried various methods, such as using FlaskForm to verify user information but ultimately, we were able use the Flask LoginManager to handle the process. Our major roadblock here was to find a way to connect the SQLite/SQLAlchemy database with the Flask server that we had the website running on. As this was our first time learning so many new concepts (HTML, CSS, Flask, SQLite etc.) and configuring/installing packages and software, it took a while to get the webiste to a working condition. As such, our results were limited, but once we were able to get past the database connection, it became significantly easier. A little more time would have gone a long way.

Another difficulty we faced during the development of the website was not being able to bring our entire idea to life. We were not able to complete the add item/add closet process, or display the closets and items that were inputted by the user. We had many ideas, such as allowing users to like or dislike outfits that were generated or being able to generate outfits based on the weather. Unfortunately, due to time constraints and overall limitations, we had to scale back our plans.

## What we Learned/Enjoyed
This project was an excellent opportunity to expand our knowledge and learn more about different programming languages. We started with HTML, which was fairly simple to understand. However, as we further developed the website to add interactivity, we had to learn more about JavaScript and Flask, which was a bit more challenging. We were also able to learn more about CSS to style and website and make it more appealing by customizing a template to speed up the process. We found that working with these new languages allowed us to think about programming in new ways and learn new syntax. We were able to gain a better understanding of what it takes to build a simple website, and that was very rewarding to see. Although we had to cut some of our ideas, we were able to enjoy our work take shape.

## Citations
https://www.w3schools.com/w3css/w3css_templates.asp https://www.youtube.com/watch?v=dam0GPOAvVI&t=6160s - for HTML templates
https://www.youtube.com/watch?v=dam0GPOAvVI&t=537s - for Flask app set up and installation
