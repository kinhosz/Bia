import Bia
from Pages import homepage, teste

def main():

    app = Bia.App()
    home = Bia.Page(app, homepage.render)
    test = Bia.Page(app, teste.render)
    app.register("homepage", home)
    app.register("teste", test)
    app.render()

if __name__ == "__main__":
    main()