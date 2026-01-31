
NAME = "Alexander Leak"
FIELD = "Business and Financial Analytics"
INSTITUTION= "University of the Free State"

DETAILS= """
## **Hi, I'm Alex a student from UFS** 👋

#### Education

- Bcom Business and Financial Analytics 
    - 2022 - 2025
    - Stats, Finance and Coding
- Coursera Certificates:
    - Linear Algebra: Elementary to Advanced
    - Data Anlytics using Excel and R
    - Python for everybody

#### Work Experience

- QuantifyYourFuture - Intern
    - Jan 2025 - Feb 2025
    - Group work to learn us how to be quants
- UFS - Student Assistant
    - July 2025 - Present
    - student assistant stuff
- Remote Maths - Mathematics Tutor
    - Jan 2024 - Present
    - Tutor high school students doing normal and AP maths
- SAHA - Tech Table Technician
    - July 2022, 2023
    - Data capture of Hockey IPT's
"""


ABOUT_ME= """
Bcom Honours student at UFS who enjoys playing pool and coding in python and R. My academic goals are obtaining the CFA Charter and becoming a Quantitative Analyst or Developer. 


"""

TECH_STACK = """
- Primary
    - Python, R, SQL
- Secondary
    - C#, Lua, Vimscript, Bash
- Tech Stack
    - Linux, Neovim and Tmux
- Libraries/Frameworks
    - Pandas, Numpy, Scikit-Learn, Tidyverse, caret
    - Quarto/Pandoc 
"""

PUBLICATIONS = """
I'm fresh out of undergrad so none yet. Check back soon. You might see something about recommender systems.
"""

PROJECTS_TABLE = """
| Personal               | Assignment Based  |
| ---------------------- | ----------------- |
| Audio Feature Pipeline | Bayesian Network  |
| Tutorial Automater     | Churn Prediction  |
| MNIST Classification   | Anomaly Detection |
| Spam Detection         |                   |
"""

Proj_AFP = """
Extract data from `Reccobeats` api of a User's Listening History which is uploaded
as a zip file. Still a WIP and learning experience. Trying to figure out pydantic to 
implement it there
"""

Proj_QE= """
Build questions with a memo and use Quarto, jinja2 and sympy to generate parameterised 
question sets and tutorials
"""

Proj_Chess = """
Its chess. Not well done but its chess.
"""

Proj_BN = """
Consumer Subsistence dataset inference using self imposed bias structure
"""

Proj_CP = """
The Telco Dataset. Those learning curves still haunt me
"""

Proj_AD = """
Anomaly detection with custom stat metric model wrapped around `sklearn.base`
"""


__all__ = ["NAME","FIELD","INSTITUTION","ABOUT_ME","TECH_STACK","PUBLICATIONS",'DETAILS',
           'PROJECTS_TABLE','Proj_AD',"Proj_Chess","Proj_AFP","Proj_BN","Proj_CP","Proj_QE"]
