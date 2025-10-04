

class BuzzerboyArchetype:
    """
    Buzzerboy Archetype for Buzzerboy Architectures
    """


    def __init__(self, product, app, tier, organization, region='ca-central-1'):

        #lower case all inputs
        product = product.lower()
        app = app.lower()
        tier = tier.lower()
        organization = organization.lower()
        region = region.lower() 
        
        self.product = product
        self.app = app
        self.tier = tier
        self.organization = organization
        self.region = region
        self.resources = {}

    def get_tier(self):
        """
        Returns the tier of the project.
        """
        return self.tier or 'dev'

    def get_project_name(self):
        """
        Returns the project name based on the product and tier.
        """
        return f"{self.product}-{self.app}-{self.tier}"
    
    def get_secret_name(self):
        """
        Returns the project name based on the product and tier.
        """
        return f"{self.organization}/{self.tier}/{self.product}-{self.app}-{self.tier}"


    def get_region(self):
        """
        Returns the AWS region for the project.
        """
        return self.region
    

    def set_stack(self, stack):
        """
        Sets the stack for the archetype.
        """
        self.stack = stack
    def get_domain_name(self):
        """
        Returns the domain name for the project.
        """
        return f"{self.get_project_name()}.{self.organization}.com"