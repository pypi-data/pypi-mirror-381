brand_cto_sample = """ 
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

brand_meeting_response = """ 
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

brand_meeting_second_response = """ 
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

brand_shoptalk_response = """ 
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

brand_none_response = """ 
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

brand_cfo_sample = """ 
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

brand_csco_sample = """
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

retailer_csco_example = """
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

grocer_csco_example = """
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

grocer_cfo_example = """
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

grocer_cfo_example_two = """
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

grocer_cto_example = """
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

retail_cto_example = """
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

dallas_sample_first_email = """
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

dallas_sample_second_email = """
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""

general_planning_email = """
Hi, my name is Roshan. I'm a student at SJSU and am interested in connecting. CES is coming up and I wanted to explore any opportunities you have so that I could volunteer/take part in. Thank you!
"""


# emails for grocery
# grocer_cfo_example, grocer_cfo_example_two, grocer_csco_example, grocer_cto_example
# retail_cto_example, retailer_csco_example
# brand_cfo_sample, brand_cto_sample, brand_csco_sample


def get_title(title:str):
    title = title.lower()
    # Roles focused on technology, IT, and digital infrastructure
    cto = [
        "director of infrastructure information technology",
        "vp of it",
        "chief technology officer",
        "chief technology officer and cdo",
    "director of analytics",
    "engineering manager - erp",
    "cto / vp ecommerce",
    "director of product management",
    "svp, program and product management",
    "cto",
    "director of web and business intelligence engineering",
    "svp, chief digital development and unified commerce officer",
    "director of web and business intelligence engineering",
    "svp, chief digital development and unified commerce officer",
        "sr. director of technology",
        "sr vp e-commerce",
        "head of ecommerce",
        "sr.director, loyalty and martech",
        "director, product management martech",
        "gvp, digital product & ux",
        "principal solutions architect",
        "product manager",  # first occurrence
        "marketing technology platform owner",
        "director, product manager",
        "sr director, mobile engineering",
        "group product manager",
        "product manager",
        "sr. manager, digital commerce operations",
        "digital omnichannel manager",
        "vice president, digital & customer experience",
        "director - digital insights & analytics",
        "sr. director, ecommerce",
        "director digital ecommerce",
        "director, omnichannel product management",
        "acquisition marketing director",
    "ecommerce analytics manager",
    "ecommerce vp",
    "manager it (product owner shopify)",
    "regional ecommerce and innovation manager",
    "svp. it - business apps, data, dtc",
    "vp, digital & ecommerce",
    "senior product manager, user experience",
    "chief digital officer",
    "enterprise architect",
    "lead ai implementation manor.ch",
    "vp, ecommerce & crm",
    "product manager - omnichannel",
    "director digital marketing",
    "executive director, digital marketing",
    "head of performance marketing",
        "head of technology",
        "head of digital & ecommerce",
        "global director of e-commerce",
        "director- ecommerce",
        "director of ecommerce & merchandising",
        "director of ecommerce and business development",
        "director of e-commerce merchandising",
        "director, ecommerce",
        "vp of ecommerce",
        "vp, digital",
        "vice president of marketing & ecommerce",
        "vp of marketing"
    ]


    # Roles focused on finance, accounting, and overall financial strategy
    cfo = [
        "senior director of finance",
        "owner",
        "chief financial officer",
        "director of financial planning, pricing strategy and inventory management (ecommerce)",
        "vice president of finance",
        "director of inventory and cost accounting",
        "cfo",
        "cfo",
        "senior vice president of revenue",
        "cfo & coo",
        "vice president - strategy, research and insights",
        "ceo/co-founder",
        "svp, customer & revenue growth",
        "founder / ceo",
        "president",
        "vp sales & marketing",
        "vice president of sales",
        "executive director",
        "ceo curaden usa",
        "sr. director, retention",
        "evp & chief commercial officer",
        "vice president - financial planning and analysis",
        "expereince channel marketing associate",
        "director of marketing procurement",
        "chief marketing officer",
        "vp merchandising",
        "director of sales planning",
        "vp global marketing",
        "sr. director, marketing",
        "sr. manager, integrated marketing",
        "vp growth marketing",
        "cro",  # Chief Revenue Officer (finance-related)
        "chief growth officer",  # Growth and finance strategy
        "head of sales, north america",
        "vp of sales",
        "senior analyst, strategy & operations",
        "senior buyer & brand partnerships"
    ]

    # Roles focused on supply chain, planning, inventory, and retail operations
    csco = [
        "interim demand planner",
        "senior director - inventory management",
        "director of wholesale planning",
        "inventory planning manager",
        "inventory planning manager",  # duplicate if you want to retain both occurrences
        "vp, owned retail",
        "vice president of e-commerce & digital",
        "senior director of stores and retail operations-north america",
        "senior manager, ecom operations",
        "director of planning & allocation",
        "inventory analyst",
        "senior vice president operations, supply chain and emerging markets",
        "vice president of planning",
        "director of distribution and supply chain",
        "analytics & inventory manager",
        "inventory analyst",
        "svp global supply chain",
        "supply chain",
        "director of supply chain",
        "senior director, e-commerce",
        "director of ecommerce",
        "director of operations",
        "head of dtc",
        "ceo",
        "vp, growth",
        "director of dtc, martech, and digital compliance",
        "head of digital, loyalty & retention",
        "co-ceo",
        "founder and ceo",
        "chief operating officer",
        "general manager",
        "ecommerce & omnichannel dtc regional director americas",
        "director of operations",
        "north america country director",
        "director of pmo",
        "director of systems of operations",
        "chief merchandising officer",

        "head of recruiting, training and development",
        "coo",
        "head of retail",
        "director of retail operations",
        "sr. director, retail vm",
        "supply chain operations",
        "co-founder",
        "co-founder & co-ceo",

        "director of brand marketing / social media, favorite daughter",
        "sr director of ecommerce merchandising",
        "sr. manager, us/ca consumer experience, omnichannel & innovation",
        "senior director of operations",
        "executive director, omnichannel",
        "director of qa",
        "vp of operations",
        "dmm of men's shoes",
        "head of business development",
        "senior project manager",
        "director of retail stores and events",
        "director of site merchandising",
        "director, product stores",
        "director/dmm",
        "executive vice president of operations",
        "head of operations",
        "managing director",
        "sr. director digital operations",
        "vp of omni operations",
        "vp, head of operations"
    ]

    if title in cto:
        return "cto"
    elif title in cfo:
        return "cfo"
    elif title in csco:
        return "csco"


def get_sample_emails(title: str, category: str, business: str):
    """
    industry can be grocer, retail, brand; title can be ceo, cfo, cto, cso.
    Return list of sample emails for the given title and industry.
    """
    generic_emails = True
    if True:
        return [general_planning_email]
    dallas_email=True
    if dallas_email:
        return [dallas_sample_first_email, dallas_sample_second_email]
    business = business.lower()
    category = category.lower()
    title = title.lower()
    email_title = get_title(title)
    is_d2c = business in ['d2c', 'direct to consumer']
    if is_d2c:
        if email_title == 'cfo' :
            return [brand_cfo_sample]
        elif email_title == 'csco':
            return [brand_csco_sample]
        elif email_title =='cto':
            return [brand_cto_sample]
    # if not d2c, then it is retailer
    if "grocer" in category:
        if email_title == 'cfo' :
            return [grocer_cfo_example, grocer_cfo_example_two]
        elif email_title == 'csco':
            primary = [grocer_csco_example]
            return primary
        elif email_title =='cto':
            return [grocer_cto_example]
    if email_title =='cto':
        return [retail_cto_example]
    elif email_title == 'csco':
        return [retailer_csco_example]
    return [retail_cto_example, retailer_csco_example]


def process_titles(file_path: str):
    import os
    import csv
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(file_path, mode="r", encoding="latin-1") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            email_title = get_title(row[4])
            if not email_title:
                print(row[4])


#process_titles("Shoptalk Outreaches-17Mar-Pending.csv")