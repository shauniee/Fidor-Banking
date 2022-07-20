from urllib import response
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from flask import Flask, request, redirect, session, url_for, render_template
import requests
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
# app.config['SECRET_KEY'] = 'Enter your own secret key'

# client_id and client_secret detmails are from the FIDOR portal.
client_id = "2830f4bc47a5b1d1"
client_secret = "Enter your own secret key"

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "forin-341512",
#   "private_key_id": "Enter your own private key id",
#   "private_key": "Enter your own private key",
  "client_email": "firebase-adminsdk-1hxem@forin-341512.iam.gserviceaccount.com",
  "client_id": "115703940268425782559",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1hxem%40forin-341512.iam.gserviceaccount.com"
})
firebase_admin.initialize_app(cred)
db = firestore.client()

authorization_base_url = 'https://apm.tp.sandbox.fidorfzco.com/oauth/authorize'
token_url = 'https://apm.tp.sandbox.fidorfzco.com/oauth/token'
redirect_uri = 'http://localhost:5000/callback'

@app.route("/forin", methods=["GET"])
def forin():
    return render_template('forin.html')

@app.route("/currency_converter", methods=["GET"])
def currency_converter():
    url1 = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=SGD&to_currency=USD&apikey=0L2OWVNK49Z0F6SS"
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=0L2OWVNK49Z0F6SS"

    response1 = requests.request("GET", url1)
    print("services2=" + response1.text)
    #convert from JSON string to Python Dictionary
    currencyData1 = json.loads(response1.text)
    SGDUSD = currencyData1["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

    response = requests.request("GET", url)
    print("services2=" + response.text)
    #convert from JSON string to Python Dictionary
    currencyData = json.loads(response.text)
    USDSGD = currencyData["Realtime Currency Exchange Rate"]["5. Exchange Rate"]


    return render_template('currency_converter.html', USD=SGDUSD, SGD=USDSGD)

@app.route("/myStocks", methods=["GET"])
def showStocks():
    docs = db.collection('myStocks').get()
    for stocks in docs:
        userStocks = stocks.to_dict()
        print(userStocks)

    nasdaqStocksUrl = "https://financialmodelingprep.com/api/v3/nasdaq_constituent?apikey=24b066c7abb4793ef5247bfa2cc44f3d"
    response4 = requests.request("GET", nasdaqStocksUrl)
    print("services4=" + response4.text)
    recommendedNASDAQStocks = json.loads(response4.text)
    showNASDAQRecommended = recommendedNASDAQStocks[0]['symbol']
    showNASDAQName = recommendedNASDAQStocks[0]['name']
    showNASDAQSector = recommendedNASDAQStocks[0]['sector']
    showNASDAQFounded = recommendedNASDAQStocks[0]['founded']

    showNASDAQRecommended1 = recommendedNASDAQStocks[1]['symbol']
    showNASDAQName1 = recommendedNASDAQStocks[1]['name']
    showNASDAQSector1 = recommendedNASDAQStocks[1]['sector']
    showNASDAQFounded1 = recommendedNASDAQStocks[1]['founded']

    showNASDAQRecommended2 = recommendedNASDAQStocks[2]['symbol']
    showNASDAQName2 = recommendedNASDAQStocks[2]['name']
    showNASDAQSector2 = recommendedNASDAQStocks[2]['sector']
    showNASDAQFounded2 = recommendedNASDAQStocks[2]['founded']

    showNASDAQRecommended3 = recommendedNASDAQStocks[3]['symbol']
    showNASDAQName3 = recommendedNASDAQStocks[3]['name']
    showNASDAQSector3 = recommendedNASDAQStocks[3]['sector']
    showNASDAQFounded3 = recommendedNASDAQStocks[3]['founded']

    showNASDAQRecommended4 = recommendedNASDAQStocks[4]['symbol']
    showNASDAQName4 = recommendedNASDAQStocks[4]['name']
    showNASDAQSector4 = recommendedNASDAQStocks[4]['sector']
    showNASDAQFounded4 = recommendedNASDAQStocks[4]['founded']

    showNASDAQRecommended5 = recommendedNASDAQStocks[5]['symbol']
    showNASDAQName5 = recommendedNASDAQStocks[5]['name']
    showNASDAQSector5 = recommendedNASDAQStocks[5]['sector']
    showNASDAQFounded5 = recommendedNASDAQStocks[5]['founded']

    showNASDAQRecommended6 = recommendedNASDAQStocks[6]['symbol']
    showNASDAQName6 = recommendedNASDAQStocks[6]['name']
    showNASDAQSector6 = recommendedNASDAQStocks[6]['sector']
    showNASDAQFounded6 = recommendedNASDAQStocks[6]['founded']

    showNASDAQRecommended7 = recommendedNASDAQStocks[7]['symbol']
    showNASDAQName7 = recommendedNASDAQStocks[7]['name']
    showNASDAQSector7 = recommendedNASDAQStocks[7]['sector']
    showNASDAQFounded7 = recommendedNASDAQStocks[7]['founded']

    showNASDAQRecommended8 = recommendedNASDAQStocks[8]['symbol']
    showNASDAQName8 = recommendedNASDAQStocks[8]['name']
    showNASDAQSector8 = recommendedNASDAQStocks[8]['sector']
    showNASDAQFounded8 = recommendedNASDAQStocks[8]['founded']

    showNASDAQRecommended9 = recommendedNASDAQStocks[9]['symbol']
    showNASDAQName9 = recommendedNASDAQStocks[9]['name']
    showNASDAQSector9 = recommendedNASDAQStocks[9]['sector']
    showNASDAQFounded9 = recommendedNASDAQStocks[9]['founded']

    return render_template('myStocks.html', uStocks = userStocks, 
    nRecommended = showNASDAQRecommended, nName = showNASDAQName, nSector = showNASDAQSector, nFounded = showNASDAQFounded,
    nRecommended1 = showNASDAQRecommended1, nName1 = showNASDAQName1, nSector1 = showNASDAQSector1, nFounded1 = showNASDAQFounded1,
    nRecommended2 = showNASDAQRecommended2, nName2 = showNASDAQName2, nSector2 = showNASDAQSector2, nFounded2 = showNASDAQFounded2,
    nRecommended3 = showNASDAQRecommended3, nName3 = showNASDAQName3, nSector3 = showNASDAQSector3, nFounded3 = showNASDAQFounded3,
    nRecommended4 = showNASDAQRecommended4, nName4 = showNASDAQName4, nSector4 = showNASDAQSector4, nFounded4 = showNASDAQFounded4,
    nRecommended5 = showNASDAQRecommended5, nName5 = showNASDAQName5, nSector5 = showNASDAQSector5, nFounded5 = showNASDAQFounded5,
    nRecommended6 = showNASDAQRecommended6, nName6 = showNASDAQName6, nSector6 = showNASDAQSector6, nFounded6 = showNASDAQFounded6,
    nRecommended7 = showNASDAQRecommended7, nName7 = showNASDAQName7, nSector7 = showNASDAQSector7, nFounded7 = showNASDAQFounded7,
    nRecommended8 = showNASDAQRecommended8, nName8 = showNASDAQName8, nSector8 = showNASDAQSector8, nFounded8 = showNASDAQFounded8,
    nRecommended9 = showNASDAQRecommended9, nName9 = showNASDAQName9, nSector9 = showNASDAQSector9, nFounded9 = showNASDAQFounded9)

@app.route('/login', methods=["GET"])
def default():
    try:
        #Step 1: User Application Authorization    
        #sending authorization client ID and client Secret to Fidor for authorization
        fidor = OAuth2Session(client_id,redirect_uri=redirect_uri)
        authorization_url, state = fidor.authorization_url(authorization_base_url)
        # State is used to prevent CSRF, keep this for later.
        session['oauth_state'] = state
        print("authorization URL is =" +authorization_url)
        return redirect(authorization_url)
    except KeyError:
        print("Key error in default-to return back to home")
        return redirect(url_for('default'))

@app.route("/callback", methods=["GET"])
def callback():
    try:
        #Step 2: Retrieving an access token.
        #The user has been redirected back from the provider to your registered
        #callback URL. With this redirection comes an authorization code included
        #in the redirect URL. We will use that to obtain an access token.
        fidor = OAuth2Session(state=session['oauth_state'])
        authorizationCode = request.args.get('code')
        body = 'grant_type="authorization_code&code='+authorizationCode+ \
        '&redirect_uri='+redirect_uri+'&client_id='+client_id
        auth = HTTPBasicAuth(client_id, client_secret)
        token = fidor.fetch_token(token_url,auth=auth,code=authorizationCode,body=body,method='POST')

        # At this point you can fetch protected resources but lets save
        # the token and show how this is done from a persisted token
        session['oauth_token'] = token
        return redirect(url_for('.home'))
    except KeyError:
        print("Key error in callback-to return back to home")
        return redirect(url_for('default'))

@app.route("/home", methods=["GET"])
def home():
    #Fetching a protected resource using an OAuth 2 token.
    try:
        token =  session['oauth_token']  
        accountUrl = "https://api.tp.sandbox.fidorfzco.com/accounts"
        payload = ""
        headers = {
            'Accept': "application/vnd.fidor.de;version=1;text/json",
            'Authorization': "Bearer "+token["access_token"]
            }
        response = requests.request("GET", accountUrl, data=payload, headers=headers)
        print("services=" + response.text)
        customersAccount = json.loads(response.text)
        customerDetails = customersAccount['data'][0]
        customerInformation = customerDetails['customers'][0] 
        accountCreatedOn = customersAccount['data'][0]['created_at']
        accountUpdatedOn = customersAccount['data'][0]['updated_at'] 
        session['fidor_customer'] = customersAccount

        marketActivityUrl = "https://api.polygon.io/v1/marketstatus/now?apiKey=__aIoBB_reLd5AkTDgzpuxpGwpLlphqg"
        payload2 = ""
        headers2 = ""
        response2 = requests.request("GET", marketActivityUrl, data=payload2, headers=headers2)
        print("services2=" + response2.text)
        marketActivity = json.loads(response2.text)
        marketStatus = marketActivity['exchanges']

        recommendedStocksUrl = "https://yfapi.net/v1/finance/trending/US"
        payload3 = ""
        headers3 = {
            'X-API-KEY': "AweGb6yaOO4hcRd1cKw7laR8xfR6N6n41dX2ESvP",
            'accept': "application/json"
        }
        response3 = requests.request("GET", recommendedStocksUrl, data=payload3, headers=headers3)
        print("services3=" + response3.text)
        recommendedStocks = json.loads(response3.text)
        showRecommended = recommendedStocks['finance']['result'][0]['quotes'][0]['symbol']
        showRecommended2 = recommendedStocks['finance']['result'][0]['quotes'][1]['symbol']
        showRecommended3 = recommendedStocks['finance']['result'][0]['quotes'][2]['symbol']
        showRecommended4 = recommendedStocks['finance']['result'][0]['quotes'][3]['symbol']
        showRecommended5 = recommendedStocks['finance']['result'][0]['quotes'][4]['symbol']
        showRecommended6 = recommendedStocks['finance']['result'][0]['quotes'][5]['symbol']
        showRecommended7 = recommendedStocks['finance']['result'][0]['quotes'][6]['symbol']
        showRecommended8 = recommendedStocks['finance']['result'][0]['quotes'][7]['symbol']
        showRecommended9 = recommendedStocks['finance']['result'][0]['quotes'][8]['symbol']
        showRecommended10 = recommendedStocks['finance']['result'][0]['quotes'][9]['symbol']


        return render_template('home.html', mStatus=marketStatus['nasdaq'],
                fID=customerInformation["id"], aCO=accountCreatedOn, aUO=accountUpdatedOn,
                fFirstName=customerInformation["first_name"],fLastName=customerInformation["last_name"],
                fAccountNo=customerDetails["account_number"],fBalance=(customerDetails["balance"]/100),
                sRStocks=showRecommended, sRStocks2=showRecommended2, sRStocks3=showRecommended3, sRStocks4=showRecommended4, sRStocks5=showRecommended5, sRStocks6=showRecommended6, sRStocks7=showRecommended7, sRStocks8=showRecommended8, sRStocks9=showRecommended9, sRStocks10=showRecommended10)

    except KeyError:
        print("Key error in services-to return back to home")
        return redirect(url_for('default'))

@app.route("/transactionHistory", methods=["GET"])
def transactionHistory():
    #Fetching a protected resource using an OAuth 2 token.
    try:
        token =  session['oauth_token']  
        url = "https://api.tp.sandbox.fidorfzco.com/internal_transfers"

        payload = ""
        headers = {
            'Accept': "application/vnd.fidor.de;version=1;text/json",
            'Authorization': "Bearer "+token["access_token"],
            'Content-Type': "application/json"
            }

        response = requests.request("GET", url, data=payload, headers=headers)
        print("services=" + response.text)
        accountTransaction = json.loads(response.text)
        listData = accountTransaction["data"]
        print("hi")
        print(listData)
        transactionId = listData[0]["external_uid"]
        transactionTime = listData[0]["created_at"]
        transactionSubject = listData[0]["subject"]
        transactionFrom = listData[0]["account_id"]
        transactionTo = listData[0]["receiver"]
        transactionAmount = listData[0]["amount"]

        return render_template('transactionHistory.html',tID=transactionId, tTime=transactionTime,
                tSubject=transactionSubject, tFrom=transactionFrom,tTo=transactionTo, tAmount=(transactionAmount/100) )

    except KeyError:
        print("Key error in services-to return back to home")
        return redirect(url_for('default'))

@app.route("/bank_transfer", methods=["GET"])
def transfer():
    try:
        customersAccount = session['fidor_customer']
        customerDetails = customersAccount['data'][0]

        return render_template('internal_transfer.html',fFIDORID=customerDetails["id"],
            fAccountNo=customerDetails["account_number"],fBalance=(customerDetails["balance"]/100))

    except KeyError:
        print("Key error in bank_transfer-to return back to home")
        return redirect(url_for('.home'))


@app.route("/process", methods=["POST"])
def process():

    if request.method == "POST":
        token =  session['oauth_token']         
        customersAccount = session['fidor_customer']
        customerDetails = customersAccount['data'][0]

        fidorID = customerDetails['id']
        custEmail = 'studentB10@email.com'
        transferAmt = int(float(request.form['transferAmount'])*100)
        transferRemarks = request.form['stockName']
        transactionID = request.form['transactionID']
        stockVolume = request.form['stockVolume']

        url = "https://api.tp.sandbox.fidorfzco.com/internal_transfers"
        payload = "{\n\t\"account_id\": \""+fidorID+"\",\n\t\"receiver\": \""+ \
                custEmail+"\",\n\t\"external_uid\": \""+transactionID+"\",\n\t\"amount\": "+ \
                str(transferAmt)+",\n\t\"subject\": \""+transferRemarks+"\"\n}\n"
        headers = {
            'Accept': "application/vnd.fidor.de; version=1,text/json",
            'Authorization': "Bearer "+token["access_token"],
            'Content-Type': "application/json"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        print("process="+response.text)

        transactionDetails = json.loads(response.text)
        print(transactionDetails)

        data={u'stock': transferRemarks, u'volume': stockVolume}
        db.collection(u'myStocks').document(transactionID).set(data)

    return render_template('transfer_result.html', fTransactionID=transactionDetails["id"],
            custEmail=transactionDetails["receiver"],fRemarks=transactionDetails["subject"],
            famount=(float(transactionDetails["amount"])/100),
            fRecipientName=transactionDetails["recipient_name"])


@app.route("/stock", methods=["GET"])
def stock():
    url = "https://finnhub.io/api/v1/news"

    querystring = {'token': "c88v06qad3ia349rkm50", "category":"general"}

    response = requests.request("GET", url, params=querystring)
    print("services=" + response.text)
    newsArticles = json.loads(response.text)
    listNews = newsArticles
    News1 = listNews[0]['headline']
    Link1 = listNews[0]['url']
    Image1 = listNews[0]['image']

    News2 = listNews[1]['headline']
    Link2 = listNews[1]['url']
    Image2 = listNews[1]['image']

    News3 = listNews[2]['headline']
    Link3 = listNews[2]['url']
    Image3 = listNews[2]['image']

    News4 = listNews[3]['headline']
    Link4 = listNews[3]['url']
    Image4 = listNews[4]['image']

    News5 = listNews[4]['headline']
    Link5 = listNews[4]['url']
    Image5 = listNews[4]['image']

    News6 = listNews[5]['headline']
    Link6 = listNews[5]['url']
    Image6 = listNews[5]['image']

    News7 = listNews[6]['headline']
    Link7 = listNews[6]['url']
    Image7 = listNews[6]['image']

    News8 = listNews[7]['headline']
    Link8 = listNews[7]['url']
    Image8 = listNews[7]['image']

    News9 = listNews[8]['headline']
    Link9 = listNews[8]['url']
    Image9 = listNews[8]['image']

    News10 = listNews[9]['headline']
    Link10 = listNews[9]['url']
    Image10 = listNews[9]['image']

    return render_template('stock.html', N1=News1, U1=Link1, I1=Image1, 
    N2=News2, U2=Link2, I2=Image2, 
    N3=News3, U3=Link3, I3=Image3,
    N4=News4, U4=Link4, I4=Image4,
    N5=News5, U5=Link5, I5=Image5,
    N6=News6, U6=Link6, I6=Image6,
    N7=News7, U7=Link7, I7=Image7,
    N8=News8, U8=Link8, I8=Image8,
    N9=News9, U9=Link9, I9=Image9,
    N10=News10, U10=Link10, I10=Image10)


@app.route('/stocksearch', methods=['GET', 'POST'])
def stocksearch():
    error = None
    if request.method == "POST":
        tickerCode = request.form['stockSymbol']
        api_key = '0L2OWVNK49Z0F6SS'
        url = "https://www.alphavantage.co/query"

        querystring = {"function":"TIME_SERIES_INTRADAY","symbol":tickerCode,"interval":"5min","apikey":api_key}

        payload = ""
        headers = {'cache-control': "no-cache"}

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        #convert from JSON string to Python Dictionary
        stockData = json.loads(response.text)
        #To retrieve the latest date from Meta Data
        lastRefreshedDate = stockData["Meta Data"]["3. Last Refreshed"]
        #To retrieve lastest stock price
        latestStockPrices = stockData["Time Series (5min)"][lastRefreshedDate]
        #closingPrice = latestStockPrices["4. close"]
        closingPrice = stockData["Time Series (5min)"][lastRefreshedDate]["4. close"]
        #volume = latestStockPrices["5. volume"]
        volume = stockData["Time Series (5min)"][lastRefreshedDate]["5. volume"]

        querystring2 = {"function": "OVERVIEW","symbol":tickerCode,"apikey":api_key}
        payload2 = ""
        headers2 = ""
        response2 = requests.request("GET", url, data=payload2, headers=headers2, params=querystring2)
        print("services2=" + response2.text)
        stockDetail = json.loads(response2.text)
        stockDescription = stockDetail['Description'] 
        stockName = stockDetail['Name']
        stockSector = stockDetail['Sector']
        stockPE = stockDetail['PERatio']
        stockPB = stockDetail['PriceToBookRatio']
        stockDPS = stockDetail['DividendPerShare']
        stockPM = stockDetail['ProfitMargin']
        stockBeta = stockDetail['Beta']



        return render_template('stock_price.html',tCode=tickerCode, sPrice=closingPrice, cVolume=volume, dTime=lastRefreshedDate, 
        sDescription=stockDescription, sName=stockName, sSector=stockSector, sPE=stockPE, sPB=stockPB, sDPS=stockDPS, sPM=stockPM, sBeta=stockBeta)

@app.route('/currency_rate', methods=['GET', 'POST'])
def currency_rate():
    error = None
    if request.method == "POST":
        firstCurrencyCode = request.form['firstCurrencySymbol']
        secondCurrencyCode = request.form['secondCurrencySymbol']
        totalAmount = request.form['exchangeAmount']
        url = "https://api.exchangerate.host/convert"

        querystring = {"from":firstCurrencyCode, "to": secondCurrencyCode}


        response = requests.request("GET", url, params=querystring)
        print("services=" + response.text)

        #convert from JSON string to Python Dictionary
        currencyData = json.loads(response.text)
        fromCurrencyExchange = currencyData["query"]["from"]
        toCurrencyExchange = currencyData["query"]["to"]
        #To retrieve conversion rate
        latestCurrencyRates = currencyData["info"]["rate"]

        print(latestCurrencyRates)
        exchangeAmount = float(totalAmount)*latestCurrencyRates
        print(exchangeAmount)


    return render_template('currency_converter.html',fCurrency=fromCurrencyExchange, tCurrency=toCurrencyExchange, lRate = latestCurrencyRates, eAmount=exchangeAmount, tAmount=float(totalAmount))

       