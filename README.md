# benj-datsci-tutorials
A git repo for Calvin and Benjamin Lawson to share code. 

## Local Jupyter Notebook Environment

In order to stand up a local instance of Jupyter notebook run this command:

```bash
docker compose up
```

Once that stand up you should see something like this:

```
benj-datsci-tutorials-local-dev-1  | [C 2023-07-13 19:11:23.399 ServerApp]
benj-datsci-tutorials-local-dev-1  | 
benj-datsci-tutorials-local-dev-1  |     To access the server, open this file in a browser:
benj-datsci-tutorials-local-dev-1  |         file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
benj-datsci-tutorials-local-dev-1  |     Or copy and paste one of these URLs:
benj-datsci-tutorials-local-dev-1  |         http://373bd93cd2a1:8888/lab?token=40a0a14478737b182a7233e250c85e711e0c85c6d8036604
benj-datsci-tutorials-local-dev-1  |         http://127.0.0.1:8888/lab?token=40a0a14478737b182a7233e250c85e711e0c85c6d8036604
```

If you click on the last link, the one that goes to localhost/127.0.0.1 it will take you to the Jupyter Notebook.
