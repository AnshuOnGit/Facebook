import httplib2
import sys

def print_my_posts(username, password):
    client = httplib2.Http()
    #client = add_credentials(username, password)
    
    response, content = client.request('https://graph.facebook.com/me/photos?access_token='+ "CAACEdEose0cBAHbN4emHtGeyZCh66MoAO2l5HYSL6yQz3Je8D23pvoZBZCntECiZAJB6T2X9iPuRpcNfwhwHnnkEzJhcWlnSUCcFXncgxr94QqccpbZB2pL7q7J4Oz3NcuJZC1GO9059fqZBZALcg7Tk64vA6E0zPw1scvmOEL3ZAy6SyrTaIdzRFD18camMRxx5EtHwOh6M3ZAQZDZD")
    print("Printing response.........{0}".format(response))
    print("Printing content.........{0}".format(content))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {0} [username] [passwoord]".format(sys.argv[0]))
        sys.exit("You stupid !!! you didn't give any parameter to me and you expecting me to work normally huh???")
    
    username, password = sys.argv[1: ]
    print_my_posts(username, password)
