class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY ='2d2862a8e6fc4a96a4cfca9175d196a7'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey={}' 



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True