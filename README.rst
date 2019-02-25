Hygge ('Cozzy') Response 
=========================

.. contents:: Topics

.. image:: https://foobar.svg
  :target: https://foobare

Overview
--------


website: `hygge <https://github.com/Proteusiq/hygge>`_.

.. code-block:: shell-session

   # install hygge
   pip install hygge
   
How to use

.. code-block:: python

    from hygge.get import GetResponse

    url = 'https://www.trustpilot.com/businessunit/search'
    params = {'country': 'dk', 'query': 'mate.bike'}

    res = GetResponse(url).get(params=params)
    info_url = f'https://www.trustpilot.com/businessunit/{res["businessUnits"][0]["id"]}/companyinfobox'
    print(GetResponse(info_url).get())
    
