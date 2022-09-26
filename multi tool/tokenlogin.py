from selenium import webdriver

driver = webdriver.Chrome(r"chromedriver.exe")
driver.get("https://discord.com/login")
token = "NzkzMjAzOTY1Nzg0MzU4OTMz.X-o2zQ.gZSao45rqEn-TJxkRDCAZQZ5RnE"
script = 'let token= "' + token + '";function login(e){setInterval(()=>{document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token=`"${e}"`},50),setTimeout(()=>{location.reload()},2500)}login(token);'
driver.execute_script(script)