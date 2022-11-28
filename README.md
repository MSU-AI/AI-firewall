<h1>The URL Scanner</h1>
<p>
  <img src="https://img.shields.io/github/license/MSU-AI/AI-firewall?color=%237CFC00">
  <img src="https://img.shields.io/github/contributors/MSU-AI/AI-firewall?color=%23ccff00">
  <img src="https://img.shields.io/github/stars/MSU-AI/AI-firewall?color=%237CFC00">
  <img src="https://img.shields.io/github/commit-activity/m/MSU-AI/AI-firewall?color=%23ccff00">
</p>

The purpose of our project is to develop a **Web Application Security Service** for the AI Club and any other person that wishes to use. 

In the journey of creating this security framework, we saw the importance of the URLs for WAFs, and so we decided to focus our efforts in it. 

From our studies of bad HTTP requests to server-side with common attacks such as LFIs, RFIs, and XSS, we noticed that the URLs comprised the main way of identifying the same. This also happened for client-side attacks, related to phishing and spam. So, we decided to focus on their identification and categorization.

![url_scanner](https://user-images.githubusercontent.com/95195316/204367436-4107ba52-2f29-4dc9-ab3a-48af7bc67308.gif)

<h2>Github Contributors</h2>

<table>
  <tbody>
    <tr>
      <td align="center">
        <a href="https://github.com/Y0uk1tsun3">
        <img src="https://avatars.githubusercontent.com/u/95195316" width="100px;">
        </a><br/>
        <small><b>Y0uk1tsun3</b></small>
      </td>
      <td align="center">
        <a href="https://github.com/felixliang50779">
        <img src="https://avatars.githubusercontent.com/u/112431235" width="100px;">
        </a><br/>
        <small><b>felixliang50779</b></small>
      </td>
      <td align="center">
        <a href="https://github.com/satyabyreddy">
        <img src="https://avatars.githubusercontent.com/u/102766717" width="100px;">
        </a><br/>
        <small><b>satyabyreddy</b></small>
      </td>
      <td align="center">
        <a href="https://github.com/pprahlada">
        <img src="https://avatars.githubusercontent.com/u/93998803" width="100px;">
        </a><br/>
        <small><b>pprahlada</b></small>
      </td>
    </tr>
  </tbody>
</table>

<h2>Who We Are</h2>
Felipe Marques Allevato | Computer Science | Sophomore | Cybersecurity Lover<br>
Felix | Computer Science | Junior | Aspiring Algorithm Engineer<br>
Pramod | major | year | interests<br>
Satya Byreddy | Computer Science | Junior | Machine Learning Enthusiast<br>
<p></p>

# How to set up the App
## 1. First, clone the repository
```
git clone https://github.com/MSU-AI/AI-Firewall
```
Then, remember to have all the requirements installed, for this run the code bellow.
```
python3 -m pip install -r requirements.txt
```
## 2. Prepare your dataset or use the pre-built model
Take a look on the notebooks. The data preparation one will help you create your own dataset and the ML WAF one will help you understand the theory and create your own model!

If you just want to run the application, unpack the zip file and use the pre-generated pkl file :).

## 3. Running
Check in the utils.py for the port chosen, after that just run the program with flask.
```
flask --app URL_scanner run
```

If it does not work, use python to run it.
```
python3 URL_scanner.py
```

