# Python Fundamentals -- Day 1 Notes

## Resources

-   **Video:** https://www.youtube.com/watch?v=K5KVEU3aaeQ&t=3273s
-   **Documentation (Beginner):** https://www.w3schools.com/python/

------------------------------------------------------------------------

## Interview Questions & Answers

  ----------------------------------------------------------------------------------
  \#   Question             Interview Answer (1--2 lines)      Real-life Example
  ---- -------------------- ---------------------------------- ---------------------
  1    **What is a          A function is a reusable block of  Like a coffee
       function?**          code that performs a specific task machine---you press a
                            and can be called whenever needed. button, and it makes
                                                               coffee every time
                                                               without rebuilding
                                                               the machine.

  2    **Why do we use      Parameters allow a function to     Like entering
       parameters?**        work with different inputs instead different
                            of using fixed values, making it   destinations into
                            reusable and flexible.             Google Maps---it uses
                                                               the same navigation
                                                               system for every
                                                               trip.

  3    **Difference between A list stores ordered items        A shopping list vs. a
       a list and a         accessed by index, while a         phone contacts app
       dictionary?**        dictionary stores key-value pairs  (find a contact by
                            accessed by unique keys.           name, not by
                                                               position).

  4    **When would an AI   AI applications use dictionaries   A chatbot storing
       application use a    to quickly map keys to values,     `"John"` → chat
       dictionary?**        such as words to meanings, user    history or `"en"` →
                            IDs to preferences, or labels to   English language
                            predictions.                       settings.

  5    **Difference between A `for` loop is used when the      Reading every page in
       `for` and `while`    number of iterations is known,     a book (`for`)
       loops?**             while a `while` loop runs until a  vs. waiting at a
                            condition becomes false.           traffic signal until
                                                               it turns green
                                                               (`while`).

  6    **What is a class?** A class is a blueprint for         A house
                            creating objects with similar      blueprint---many
                            properties (data) and behaviors    houses can be built
                            (methods).                         from the same design.

  7    **Why do AI          Functions reduce code duplication, Instead of writing
       engineers write      improve readability, simplify      the same recipe every
       functions instead of debugging, and make maintenance    time, you keep one
       repeating code?**    easier.                            recipe and reuse it
                                                               whenever you cook.

  8    **Why do we use      f-strings are more readable,       Like filling blanks
       f-strings instead of automatically handle data types,   in a sentence
       `+` or `,`?**        and allow expressions directly     template instead of
                            inside the string.                 manually joining
                                                               words together.

  9    **What are Python    Python implementations are         Different car engines
       implementations?**   different programs that execute    (petrol, diesel,
                            Python code, each optimized for    electric) all drive a
                            different platforms or performance car but work
                            needs.                             differently
                                                               internally.

  10   **Which Python       **CPython** is the standard and    It's like using
       implementation is    most widely used implementation    Microsoft Word for
       the best?**          because it has the best            documents---it isn't
                            compatibility with Python          the only option, but
                            libraries and tools.               it's the standard.

  11   **Why does `input()` `input()` returns a string because A paper form only
       return a string?**   keyboard input is received as      records what you
                            text, and Python lets the          write; the reader
                            programmer decide how to interpret decides whether
                            it.                                `"1234"` is a PIN,
                                                               age, or ID.
  ----------------------------------------------------------------------------------

------------------------------------------------------------------------

## Key Takeaways

-   Use **functions** to write reusable code.
-   Use **parameters** to make functions flexible.
-   Use **lists** for ordered collections and **dictionaries** for
    key-value lookups.
-   Prefer **`for` loops** for known iterations and **`while` loops**
    for condition-based repetition.
-   Think of **classes** as blueprints for creating objects.
-   Prefer **f-strings** for readable string formatting.
-   **CPython** is the standard Python implementation.
-   Always remember that **`input()` returns a string**, so convert it
    with `int()` or `float()` when needed.
