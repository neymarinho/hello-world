from Fifa14Client import LoginManager
from Fifa14Client import WebAppFunctioner
import ConfigParser


def do_main():
    Config = ConfigParser.ConfigParser()
    Config.read("accounts_example.ini")
    for section in Config.sections():
        email = Config.get(section, 'Email')
        password = Config.get(section, 'Password')
        security_hash = Config.get(section, 'SecurityHash')
        form_data = eval(Config.get(section, 'FormData'))

    login = LoginManager.LoginManager(email,password,security_hash,form_data)
    print login.login()
    func = WebAppFunctioner.WebAppFunctioner(login)
    print func.get_coin_amount()
    A=1
    while A > 0:
        for  card in func.search("training", "", "", "", "", "", "", "", "","1000", "255", "",0,"playStyle","",""):
            if func.bid(card.tradeId,card.buyNowPrice):
                print 'OL bought for'
                if func.move(card.id, 'trade'):
                    func.list_card(card.id, "1200", "1300", "3600")
                    print 'OL listed for'
        for  card in func.search("player", "gold", "", "", "", "", "", "", "","4100", "", "",0,"","","188152"):
            if func.bid(card.tradeId,card.buyNowPrice):
                print 'Oscar bought for'
                if func.move(card.id, 'trade'):
                    func.list_card(card.id, "4400", "4500", "3600")
                    print 'Oscar listed for'
        for  card in func.search("player", "gold", "", "", "", "", "", "", "","11000", "", "",0,"","","181820"):
            if func.bid(card.tradeId,card.buyNowPrice):
                print 'Jovetic bought for'
                if func.move(card.id, 'trade'):
                    func.list_card(card.id, "11750", "12000", "3600")
                    print 'Jovetic listed for'
        for  card in func.search("player", "gold", "", "", "", "", "", "", "","7000", "", "",0,"","","181820"):
            if func.bid(card.tradeId,card.buyNowPrice):
                print 'Lucas bought for'
                if func.move(card.id, 'trade'):
                    func.list_card(card.id, "7400", "7500", "3600")
                    print 'Lucas listed'
        for  card in func.search("player", "gold", "", "", "", "", "", "", "","3400", "", "",0,"","","164859"):
            if func.bid(card.tradeId,card.buyNowPrice):
                print 'Walcott bought for'
                if func.move(card.id, 'trade'):
                    func.list_card(card.id, "3700", "3800", "3600")
                    print 'Walcott listed'
        for  card in func.search("player", "gold", "RM", "", "", "", "", "", "","4300", "", "",0,"","","164859"):
            if func.bid(card.tradeId,card.buyNowPrice):
                print 'Walcott RM bought for'
                if func.move(card.id, 'trade'):
                    func.list_card(card.id, "4700", "4800", "3600")
                    print 'Walcott RM listed'
        for  card in func.get_tradepile():
             func.remove_from_tradepile(card.tradeId)

def testy():
        
                while 1:
                        try:
                                do_main()
                        except Exception, e:
                                print'EXCEPTOION OCCURED:' + str(e)


if __name__ == "__main__":
    testy()

