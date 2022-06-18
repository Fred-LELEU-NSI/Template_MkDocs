Template MkDocs minimaliste.

Amusez-vous bien !



Une console

```pycon
>>> a = 2
>>> a
2
```


!!! ugli-exo "Script interne dans admonition"

    ```python
    print("Hé, salut !")
    ```

!!! ugli-exo "Script externe dans admonition"

    {{py_admo("hello_admo")}}
    


??? ugli-exo "Script externe dans _collapsible admonition_"

    {{py_admo("hello_admo")}}


!!! ugli-exo "Scripts externes dans admonition avec onglets"

    === "C++" 
    
        {{script_admo_details("c++","scripts/hello.cpp")}}

    === "Python"

        {{py_admo_details("hello_admo")}}
