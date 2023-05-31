# Documentation and Set-up Instructions

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

Backend: SQLAlchemy/SQLite, Flask framework

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


