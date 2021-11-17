# Week4

# Reminder
When we run a script/program in the Unix environment there are standard streams recognized by a computer program.
- Standard input or `stdin` is a stream data (often text) going into a program. Unless redirected, standard input is expected from the keyboard which started the program.
- Standard output or stdout is the stream where a program writes its output data. Unless redirected, standard output is the text terminal which initiated the program.
- Standard error or `stderr` is another output stream typically used by programs to output error messages or diagnostics. Is is a stream independent of standard output and can provide error messages even when `stdout` has been redirected. `stderr` can also be redirected separately.

Redirected two different streams:
1. my_script.sh -> program_output.txt
2. my_script.sh -> error_messages.txt
`my_program | my_script.sh 1>program_output.txt 2>error_messages.txt`