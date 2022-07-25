import data 

#? Loop through the colors data and display logo image and company name on an html page. 
#* to run the file:  python3 colorsProblem.py > index.html

companies = data.data

html = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>  
    
        body{
            margin:0px;
        }
        div{
            height: 50px;
        }
    </style>
</head>
<body>
"""

for i in companies:
    business = i['business_name']
    logo = i['logo']
    html+=f"""
    <div style='font-size:60px;'>{business} </div>\n"
    <img src='{logo}' alt=''>\n"""

html += """

</body>
</html>

"""

print(html)