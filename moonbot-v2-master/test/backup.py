
async def main():    
    api_key = os.environ.get('binance_api')
    api_secret = os.environ.get('binance_secret')
    client = await AsyncClient.create(api_key, api_secret)     
    bm = BinanceSocketManager(client)
    token='BTC'
    while True:
        res = await bm.kline_socket(symbol=token+'USDT').recv()
        print('symbol: ',res['s'],' date: ',timestamp_to_datetime(res['k']['T']), ' closing price: ',res['k']['c'] , ' volume: ',res['k']['V'])
        
        investimento = 15
        leverage = 1
        minimo_guadagno_assoluto = 1
        percentuale_minimo_guadagno = 0.002     
        open_orders = []
        numero_massimo_ordini = 2
        my_symbols = ['ETH','BTC']  

        for symbol in my_symbols:
            print(symbol)

            guadagno_assoluto = abs(usdtheter-usdbinance) * investimento * leverage
            guadagno_percentuale = guadagno_assoluto/investimento
            
            print('date: ',timestamp_to_datetime(res['k']['T']), ' closing price: ',res['k']['c'] , ' volume: ',res['k']['V'])

            print('-'*80+'\nsimbolo: ',symbol)
            print('\nPREZZO in Theter \tUSDT \t: ',usdtheter['price'],'\nprezzo in binance USD\tBUSD \t: ',usdbinance['price'])
            print('\nguadagno ASSOLUTO\t: ',round(guadagno_assoluto,5),'$')
            print('\nguadagno PERCENTUALE\t: ',round(guadagno_percentuale,7),'%\n')

            busd_info = client.get_symbol_info(symbol+'USDT')
            usdt_info = client.get_symbol_info(symbol+'BUSD')
            busd_min_quantity = busd_info['filters'][2]['minQty']
            usdt_min_quantity = usdt_info['filters'][2]['minQty']
            
            print('QUANTITA MINIME ', busd_min_quantity,usdt_min_quantity)

            if len(open_orders) < numero_massimo_ordini:
                if float(guadagno_percentuale) >= percentuale_minimo_guadagno:
                    print('\n**** APRO OPERAZIONE ****\n')

                    if usdtheter['price'] > usdbinance['price']:
                        print('eseguo operazione con BUSD')
                        coin_quantity = investimento/float(usdbinance['price'])
                        order = client.order_limit_buy(timeInForce='GTC',
                            symbol = symbol+'BUSD',
                            quantity = format_coin_quantity(coin_quantity),
                            price = round(float(usdbinance['price']),2))

                    if usdtheter['price'] < usdbinance['price']:
                        print('eseguo operazione con USDT')
                        coin_quantity = investimento/float(usdtheter['price'])
                        order = client.order_limit_buy(timeInForce='GTC',
                            symbol=i+'USDT',
                            quantity = format_coin_quantity(coin_quantity),
                            price=round(float(usdtheter['price']),2))

                    open_orders.append(order)
            
                if my_order['executedQty'] == my_order['origQty']: # SE GLI ORDINI SONO STATI FILLATI 
                    if 'USDT' in my_order['symbol'] :
                        coin_quantity = investimento/float(usdtheter['price'])
                        order = client.order_limit_sell(timeInForce='GTC',
                            symbol=i+'BUSD',
                            quantity = format_coin_quantity(coin_quantity),
                            price=round(float(usdbinance['price']),2))

                    if 'BUSD' in my_order['symbol'] :
                        coin_quantity = investimento/float(usdtheter['price'])
                        order = client.order_limit_sell(timeInForce='GTC',
                            symbol=symbol+'USDT',
                            quantity = format_coin_quantity(coin_quantity),
                            price=round(float(usdtheter['price']),2))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
