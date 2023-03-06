## trie ...
- a tree like
- trienode
- dfs:
    - coba semua kemungkinan
    - backtrack:
        - kalau ketemu done
        - kalau belum .. coba yang lain
        - pop .. pop ..pop
```
for x in values:
    if dfs(x):
        return True
return False
```
- kita baru return false, setelah semua kemungkinan dilakukan.
