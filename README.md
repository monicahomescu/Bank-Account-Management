# Bank-Account-Management

Application that stores all the bank transactions performed on an account during a month. Each transaction is stored in the application using the following elements: `day` (of the month in which the transaction was made, between 1 and 30 for simplicity), `amount of money` (transferred, positive integer), `type` (`in` - into the account, `out` – from the account), and `description`. 

The program implements the functionalities exemplified below:

**(A) Add transaction**\
`add <value> <type> <description>`\
`insert <day> <value> <type> <description>`\
e.g.\
`add 100 out pizza` – add to the current day an `out` transaction of `100 RON` with the *"pizza"* description\
`insert 25 100 in salary` – insert to day 25 an `in` transaction of `100 RON` with the *“salary”* description

**(B) Modify transactions**\
`remove <day>`\
`remove <start day> to <end day>`\
`remove <type>`\
`replace <day> <type> <description> with <value>`\
e.g.\
`remove 15` – remove all transactions from day 15\
`remove 5 to 10` – remove all transactions between days 5 and 10\
`remove in` – remove all `in` transactions\
`replace 12 in salary with 2000` – replace the amount for the `in` transaction having the *“salary”* description from day 12 with `2000 RON`

**(C) Display transactions having different properties**\
`list`\
`list <type>`\
`list [ < | = | > ] <value>`\
`list balance <day>`\
e.g.\
`list` – display all transactions\
`list in` – display all `in` transactions\
`list > 100` - display all transactions having an amount of money `>100`\
`list = 67` - display all transactions having an amount of money `=67`\
`list balance 10` – compute the account’s balance at the end of day 10. This is the sum of all `in` transactions, from which we subtract `out` transactions occurring before or on day 10

**(D) Filter**\
`filter <type>`\
`filter <type> <value>`\
e.g.\
`filter in` – keep only `in` transactions\
`filter in 100` – keep only `in` transactions having an amount of money smaller than `100 RON`

**(E) Undo**\
`undo` – the last operation that modified program data is reversed. The user can undo all operations performed since program start by repeatedly calling this function.

Additional implementations:

- handling of `incorrect user input` by displaying error messages (the program does not crash regardless of user input)
- built-in `list` and `dict` compound types to represent entities in the problem domain and `getter` and `setter` functions to access/modify them
- use of `Python's exception mechanism`
- `specifications` for all non-UI functions (except getters and setters)
- `tests` for all non-UI functions related to functionalities (A) and (B)
- 10 `randomly generated` items in application at program startup
