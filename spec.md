# Specification for kek.py
personal CLI interface to do the things I need to do.

The command line syntax is inspired by [TaskWarrior](https://taskwarrior.org/docs/syntax/):

```
kek <command> <modifications> <misc>
```

# Commands
Commands represent a subset of shared functionality that can be controlled with
`modifications` and `misc` arguments.

## Edit
The `edit` command handles the editing of files system. 

```
kek edit <modifications> <misc>
```

### Modifications
Possible modifications include:
- `<filename>`: name/path of file to edit (relative or absolute)
- `last`: edit the last file that was edited with kek

### Misc 

N/A

## Zet 
The `edit` command handles the editing of files system. 

```
kek edit <modifications> <misc>
```

### Modifications
Possible modifications include:
- `<filename>`: name/path of file to edit (relative or absolute)
- `last`: edit the last file that was edited with kek

### Misc 

N/A
