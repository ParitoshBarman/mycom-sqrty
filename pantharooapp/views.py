from django.shortcuts import render, HttpResponse
from pantharooapp.models import History, AllowDevice, NotAllow, AvailableFiles, FileHistory, FileHistoryNotAllowSPAM
from datetime import datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your views here.
def index(request):
    return HttpResponse(f"This is Home page ...    Paritosh is a good boy")


def fileNameDatacheak(request, empid, desktopname, ipADDress, fullname, email, now, appliName, fileName):
    filedatacheckInfo = AvailableFiles.objects.filter(fileNameData=fileName).first()
    
    if filedatacheckInfo:
        saveHistory = FileHistory(FullName=fullname, ApplicationName=appliName, EmployeeID=empid, Email=email, DesktopID=desktopname, IP_Address=ipADDress, fileNameData=fileName)
        saveHistory.save()
        return HttpResponse('True')
    else:
        nowTime2 = datetime.now()
        NotAllowSaveHistory = FileHistoryNotAllowSPAM(FullName=fullname, ApplicationName=appliName, EmployeeID=empid, Email=email, DesktopID=desktopname, IP_Address=ipADDress, fileNameData=fileName)
        NotAllowSaveHistory.save()
        senderEmail = "pantharooemail@gmail.com"
        ePassword = "jqtwtlzyhajmlrkh"
        receiverEmail = "barmanpari163@gmail.com"
        # receiverEmail = "systemready2014@gmail.com"
        messagee = MIMEMultipart("alternative")
        messagee["Subject"] = f"File Alert from Pantharoo! {fullname}"
        messagee["From"] = senderEmail
        messagee["To"] = receiverEmail

        htmlHead = """<html>
        <head>
            <style>
                *{
                    margin: 0;
                    padding: 0;
                }
                .header{
                    background-color: #e05454;;
                    width: 100vw;
                    height: 54px;
                    text-align: center;
                    font-size: 42px;
                    color: yellow;
                    font-weight: bolder;
                    letter-spacing: 5px;
                }
                h1{
                    color: green;
                    margin: 10px;
                }
                .data{
                    color: blueviolet;
                }                
            </style>
        </head>"""
        htmlBody = f"""
                    <body>
            <div class="header">File Alert!</div>
            <h1>Welcome to Pantharoo</h1>
                <h2><span>Name: </span><span class="data">{fullname}</span></h2>
                <h2><span>Application Name: </span><span class="data">{appliName}</span></h2>
                <h2><span>Desktop Name: </span><span class="data">{desktopname}</span></h2>
                <h2><span>IP Address: </span><span class="data">{ipADDress}</span></h2>
                <h3><span>Employee ID: </span><span class="data">{empid}</span></h3>
                <h3><span>Email: </span><span class="data">{email}</span></h3>
                <h3><span>Current Time: </span><span class="data">{nowTime2}</span></h3>
                <h3><span>File Name: </span><span class="data">{fileName}</span></h3>
                
            <h2>Thank you for to join with us...</h2>
        </body>
    </html>
                """
        html = htmlHead + htmlBody
        part2 = MIMEText(html, "html")
        messagee.attach(part2)
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(senderEmail, ePassword)
                server.sendmail(senderEmail, receiverEmail, messagee.as_string())
                emailStatus = 'Email also successfully received.....'
                # print('Success......')
        except:
            # print('Fail....')
            emailStatus = ''
        return HttpResponse('True')


def datacheak(request, empid, desktopname, ipADDress, fullname, email, now, appliName):
    checkInfo = AllowDevice.objects.filter(FullName=fullname, EmployeeID=empid, Email=email, DesktopID=desktopname, IP_Address=ipADDress).first()
    
    if checkInfo:
        nowTime = datetime.now()
        saveHistory = History(FullName=fullname, ApplicationName=appliName, EmployeeID=empid, Email=email, DesktopID=desktopname, IP_Address=ipADDress, UserDateTime=now, ServerDateTime=nowTime)
        saveHistory.save()
        return HttpResponse(f'True-{ipADDress}')
    else:
        nowTime2 = datetime.now()
        saveNotAllow = NotAllow(FullName=fullname, ApplicationName=appliName, EmployeeID=empid, Email=email, DesktopID=desktopname, IP_Address=ipADDress, UserDateTime=now, ServerDateTime=nowTime2)
        saveNotAllow.save()
        senderEmail = "pantharooemail@gmail.com"
        ePassword = "jqtwtlzyhajmlrkh"
        receiverEmail = "barmanpari163@gmail.com"
        # receiverEmail = "systemready2014@gmail.com"
        messagee = MIMEMultipart("alternative")
        messagee["Subject"] = f"Alert from Pantharoo! {fullname}"
        messagee["From"] = senderEmail
        messagee["To"] = receiverEmail

        htmlHead = """<html>
        <head>
            <style>
                *{
                    margin: 0;
                    padding: 0;
                }
                .header{
                    background-color: #e05454;;
                    width: 100vw;
                    height: 54px;
                    text-align: center;
                    font-size: 42px;
                    color: yellow;
                    font-weight: bolder;
                    letter-spacing: 5px;
                }
                h1{
                    color: green;
                    margin: 10px;
                }
                .data{
                    color: blueviolet;
                }                
            </style>
        </head>"""
        htmlBody = f"""
                    <body>
            <div class="header">Warning!</div>
            <h1>Welcome to Pantharoo</h1>
                <h2><span>Name: </span><span class="data">{fullname}</span></h2>
                <h2><span>Application Name: </span><span class="data">{appliName}</span></h2>
                <h2><span>Desktop Name: </span><span class="data">{desktopname}</span></h2>
                <h2><span>IP Address: </span><span class="data">{ipADDress}</span></h2>
                <h3><span>Employee ID: </span><span class="data">{empid}</span></h3>
                <h3><span>Email: </span><span class="data">{email}</span></h3>
                <h3><span>Current Time: </span><span class="data">{nowTime2}</span></h3>
                <h3><span>User Time: </span><span class="data">{now}</span></h3>
                
            <h2>Thank you for to join with us...</h2>
        </body>
    </html>
                """
        html = htmlHead + htmlBody
        part2 = MIMEText(html, "html")
        messagee.attach(part2)
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(senderEmail, ePassword)
                server.sendmail(senderEmail, receiverEmail, messagee.as_string())
                emailStatus = 'Email also successfully received.....'
                # print('Success......')
        except:
            # print('Fail....')
            emailStatus = ''
        return HttpResponse('False')
    # return HttpResponse(f"Employe Name is : {fullname} Email : {email}This is Dsktop name : {desktopname} <br> This is Employee ID: {empid} IP Address is : {ipADDress} The time is : {now}")