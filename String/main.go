package main

import "fmt"

func reverseString(s string) string {
    runes := []rune(s) // Convert string to rune slice to handle multi-byte characters
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func main() {
    s := "Hello, Go!"
    fmt.Println("Original:", s)
    fmt.Println("Reversed:", reverseString(s))
}
