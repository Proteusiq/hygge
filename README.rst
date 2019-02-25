.. image:: https://github.com/Proteusiq/hygge/blob/master/hygge.png
  :target: https://github.com/Proteusiq/hygge

Hygge ('Cozzy') Response 
=========================

"A cozzy('hygge') way to get json response back asynchronously"

.. contents:: Topics

Overview
--------

It should be easy to return json response asynchronously. hygge aim to be a fuzzy-less way to do just that.
Just pass a url and 'get' arguments such as params, headers, and receive back a json response. 

website: `hygge <https://github.com/Proteusiq/hygge>`_.

.. code-block:: shell-session

   # install hygge
   pip install hygge
   
How to use

.. code-block:: python

    from hygge.get import GetResponse

    url = 'https://www.trustpilot.com/businessunit/search'
    params = {'country': 'dk', 'query': 'mate.bike'}

    # passing url and parameters 
    res = GetResponse(url).get(params=params)
    print(res)

    # passing only url
    info_url = f'https://www.trustpilot.com/businessunit/{res["businessUnits"][0]["id"]}/companyinfobox'
    print(GetResponse(info_url).get())
    
