def is_palindrome(word: str) -> bool:
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0] != word[len(word)-1]:
        return False
    else:
        return is_palindrome(word[1:len(word)-1])

def main():
    print(f"'': {is_palindrome('')}")
    print(f"'a': {is_palindrome('a')}")
    print(f"'aaa': {is_palindrome('aaa')}")
    print(f"'abba': {is_palindrome('abba')}")
    print(f"'abcdefgfedcba': {is_palindrome('abcdefgfedcba')}")
    print(f"'abc': {is_palindrome('abc')}")
    

if __name__ == '__main__':
    main(       )