function reverse(s) {
    var new_string = '';
    for (var character = 0; character < s.length; character++) {
        new_string = s[character] + new_string
    } return new_string
}
