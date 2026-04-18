PaginationSchema = {
    "limit": {
        "type": "int",
        "min": 1,
        "default": 10
    },
    "offset": {
        "type": "int",
        "min": 0,
        "default": 0
    }
}