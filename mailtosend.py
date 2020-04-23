from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText


def sendemail(to_email):
    
    # feed ur email details here
    from_email = 'sahilkumar158@gmail.com'
    password = '531#urkhool'
    subject = 'COVID19 Report and Preventions'
    sender_name = 'Sahil'
    
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['subject'] = subject
    
    # Create the body of the message (a plain-text and an HTML version).
    text = """Hi Dear,\n\nPrevention Measures from Corona: \nHere is the link you wanted:
    \nhttps://www.google.com/search?sxsrf=ALeKk00Oy2hD35yX2hRjwh20Xx5IuSQpKQ%3A1587631332829&ei=5FShXpmhMsmV4-EPwbeTmAM&q=prevention+measures+of+covid&oq=prevention+measures+of+covid&gs_lcp=CgZwc3ktYWIQAzoECCMQJzoFCAAQkQI6BQgAEIMBOgIIADoECAAQQzoHCAAQgwEQQzoHCAAQFBCHAjoGCAAQFhAeOggIABAWEAoQHlDlE1iVdWDJf2gAcAB4AIABpgOIAc8nkgEKMC4yMy40LjEuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwiZo4LNk_7oAhXJyjgGHcHbBDMQ4dUDCAw&uact=5"""
    
    
    html = """\
    <html>
      <head></head>
      <body>
        <p><br>
           You can download the COVID19 cases Report in detain in the form of pdf.<br>
           Here is the <a href="https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200420-sitrep-91-covid-19.pdf?sfvrsn=fcf0670b_4" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200420-sitrep-91-covid-19.pdf%3Fsfvrsn%3Dfcf0670b_4&amp;ved=2ahUKEwiZo4LNk_7oAhXJyjgGHcHbBDMQFjADegQIBBAB"><br><h3 class="LC20lb DKV0Md">Coronavirus Disease 2019 (COVID-19): Situation Report – 91</h3><div class="TbwUpd NJjxre"><img class="xA33Gc" alt="" height="16" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAjVBMVEX///////3M4urN4uzn8fbw9vpyr9BFlMLA2ultrM7d6/S41eZaoMk9j76LvtnW5+/f7PQmgriEuti51+Yvh7xoqM5TmMGSwNp/tNNhosYce7Do8fVEkr4OcKoAW5y20+KfxdyszeA1iLV8r80DZqEddasrfqwAXJhxosBPk7mqydgecaBAhK00eaRMiKtEr4CmAAAAs0lEQVR4AVSPAxYEQQxEs5Pusd0Ym/c/3lr/KU4VfLjAHwrCF3KhoGq3GfLMdQNNy3Zc3VMtuOEHYeTGiZXGehZ4t0LieH6m62mqudSxbwUtR99n3E5zXYSSgC5dT0+KNC2dKqqd5laomza18rTVETPZgJBdzXvMhqGmpiF9gG5sPIYVm1K9amcA8AaZUYJ6RbNlQLixbrtf1atClq1+eqqOc5/n/TxWeEFNn4Jv0usYsAEA+JQNZOIapIoAAAAASUVORK5CYII=" width="16" data-atf="1"><cite class="iUh30 bc rpCHfe tjvcx">www.who.int › docs › situation-reports › 20200420-sitrep-91-covid-19</cite></div></a> 
        <a href="https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200418-sitrep-89-covid-19.pdf?sfvrsn=3643dd38_2" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200418-sitrep-89-covid-19.pdf%3Fsfvrsn%3D3643dd38_2&amp;ved=2ahUKEwiZo4LNk_7oAhXJyjgGHcHbBDMQFjAEegQIAhAB"><br><h3 class="LC20lb DKV0Md">Coronavirus disease 2019 (COVID-19) - World Health ...</h3><div class="TbwUpd NJjxre"><img class="xA33Gc" alt="" height="16" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAjVBMVEX///////3M4urN4uzn8fbw9vpyr9BFlMLA2ultrM7d6/S41eZaoMk9j76LvtnW5+/f7PQmgriEuti51+Yvh7xoqM5TmMGSwNp/tNNhosYce7Do8fVEkr4OcKoAW5y20+KfxdyszeA1iLV8r80DZqEddasrfqwAXJhxosBPk7mqydgecaBAhK00eaRMiKtEr4CmAAAAs0lEQVR4AVSPAxYEQQxEs5Pusd0Ym/c/3lr/KU4VfLjAHwrCF3KhoGq3GfLMdQNNy3Zc3VMtuOEHYeTGiZXGehZ4t0LieH6m62mqudSxbwUtR99n3E5zXYSSgC5dT0+KNC2dKqqd5laomza18rTVETPZgJBdzXvMhqGmpiF9gG5sPIYVm1K9amcA8AaZUYJ6RbNlQLixbrtf1atClq1+eqqOc5/n/TxWeEFNn4Jv0usYsAEA+JQNZOIapIoAAAAASUVORK5CYII=" width="16" data-atf="4"><cite class="iUh30 bc rpCHfe tjvcx">www.who.int › docs › situation-reports › 20200418-sitrep-89-covid-19</cite></div></a>
       <br>Stay Home, Stay Safe, and keep Social Distancing.
       
       <br><br>
       
       Best Regards,
        </p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    
    msg.attach(MIMEText(sender_name, 'plain'))
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.close()
        response = "mail sent successfully"
        return response
    except Exception as e:
        response = "Unable to send email. Please provide valid email address"
        return False
    
    