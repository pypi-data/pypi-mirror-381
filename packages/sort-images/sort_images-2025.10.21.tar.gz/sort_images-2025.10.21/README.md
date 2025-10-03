# sort-images

A cli tool to sort images into folders by date.

The default settings will take a directory like this:
```
.
├── DSC_0056.JPG
├── DSC_0070.JPG
├── DSC_0098.JPG
├── DSC_0170.JPG
└── DSC_0265.JPG
```
and with `sort-images . .` this becomes
```
.
├── 18
│   ├── Apr
│   │   └── DSC_0265.JPG
│   ├── Mar
│   │   └── DSC_0170.JPG
│   └── May
│       ├── DSC_0056.JPG
│       ├── DSC_0070.JPG
│       └── DSC_0098.JPG
├── DSC_0056.JPG
├── DSC_0070.JPG
├── DSC_0098.JPG
├── DSC_0170.JPG
└── DSC_0265.JPG
```

1. sort-images does not delete any files (you have to do that yourself)
2. It also does not overwrite anything, so if you ran this command again, `sort-images` would only spit out an error
3. Also, running the command again would only find the files in the `.` directory, not in the `18` directory
4. Another constant of this program is that every file will be copied. If it is not an
    image or if the date field is missing, it will be copied to the `error` directory
5. The first `.` in the command specifies the source and the second `.` the destination
6. Further syntax will be shown on `sort-images -h`