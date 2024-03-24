from constants import ABORT_AL_POSITIONS, FIND_COINTEGRATED, PLACE_TRADES, MANAGE_EXITS
from func_connections import connect_to_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results
from func_entry_pairs import open_positions
from func_exit_pairs import manage_trade_exits
from func_messaging import send_message

# Main function
if __name__ == '__main__':

    # Message on start
    send_message('Bot launched successfully!')

    # Connect to client
    try:
        print("Connecting to DyDx...")
        client = connect_to_dydx()
    except Exception as e:
        print('Error connecting to client: ', e)
        send_message("Failed to connect to client.")
        exit(1)

    # Abort all open positions
    if ABORT_AL_POSITIONS:
        try:
            print('Closing all positions...')
            close_orders = abort_all_positions(client)

        except Exception as e:
            print('Error closing all positions: ', e)
            send_message(f"Error closing all positions.{e}")
            exit(1)

    # Find cointegrated pairs
    if FIND_COINTEGRATED:

        # CONSTRUCT MARKET PRICES
        try:
            print('Fetching market prices, please allow several minutes...')
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print('Error constructing market prices: ', e)
            send_message(f"Error constructing market prices {e}")
            exit(1)

        # Store Cointegrated pairs
        try:
            print('Storing cointegrated pairs...')
            store_result = store_cointegration_results(df_market_prices)
            if store_result != 'Saved':
                print('Error storing cointegrated pairs: ')
                exit(1)
        except Exception as e:
            print('Error storing cointegrated pairs: ', e)
            send_message(f"Error storing cointegrated pairs {e}")
            exit(1)
    # Run as always on
    while True:
        # Manage Exits
        if MANAGE_EXITS:
            try:
                print('Managing exits...')
                manage_trade_exits(client)

            except Exception as e:
                print('Error managing exit positions...: ', e)
                send_message(f"Error managing positions {e}")
                exit(1)

        # Place trades for opening positions
        if PLACE_TRADES:
            try:
                print('Finding trading opportunities...')
                open_positions(client)

            except Exception as e:
                print('Error trading pairs: ', e)
                send_message(f"Error trading pairs {e}")
                exit(1)
