# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.8.2/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.8.2/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build

# Include any dependencies generated for this target.
include test/CMakeFiles/testopt.dir/depend.make

# Include the progress variables for this target.
include test/CMakeFiles/testopt.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/testopt.dir/flags.make

test/CMakeFiles/testopt.dir/testfuncs.c.o: test/CMakeFiles/testopt.dir/flags.make
test/CMakeFiles/testopt.dir/testfuncs.c.o: ../test/testfuncs.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object test/CMakeFiles/testopt.dir/testfuncs.c.o"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/testopt.dir/testfuncs.c.o   -c /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/test/testfuncs.c

test/CMakeFiles/testopt.dir/testfuncs.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/testopt.dir/testfuncs.c.i"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/test/testfuncs.c > CMakeFiles/testopt.dir/testfuncs.c.i

test/CMakeFiles/testopt.dir/testfuncs.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/testopt.dir/testfuncs.c.s"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/test/testfuncs.c -o CMakeFiles/testopt.dir/testfuncs.c.s

test/CMakeFiles/testopt.dir/testfuncs.c.o.requires:

.PHONY : test/CMakeFiles/testopt.dir/testfuncs.c.o.requires

test/CMakeFiles/testopt.dir/testfuncs.c.o.provides: test/CMakeFiles/testopt.dir/testfuncs.c.o.requires
	$(MAKE) -f test/CMakeFiles/testopt.dir/build.make test/CMakeFiles/testopt.dir/testfuncs.c.o.provides.build
.PHONY : test/CMakeFiles/testopt.dir/testfuncs.c.o.provides

test/CMakeFiles/testopt.dir/testfuncs.c.o.provides.build: test/CMakeFiles/testopt.dir/testfuncs.c.o


test/CMakeFiles/testopt.dir/testopt.c.o: test/CMakeFiles/testopt.dir/flags.make
test/CMakeFiles/testopt.dir/testopt.c.o: ../test/testopt.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object test/CMakeFiles/testopt.dir/testopt.c.o"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/testopt.dir/testopt.c.o   -c /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/test/testopt.c

test/CMakeFiles/testopt.dir/testopt.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/testopt.dir/testopt.c.i"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/test/testopt.c > CMakeFiles/testopt.dir/testopt.c.i

test/CMakeFiles/testopt.dir/testopt.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/testopt.dir/testopt.c.s"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/test/testopt.c -o CMakeFiles/testopt.dir/testopt.c.s

test/CMakeFiles/testopt.dir/testopt.c.o.requires:

.PHONY : test/CMakeFiles/testopt.dir/testopt.c.o.requires

test/CMakeFiles/testopt.dir/testopt.c.o.provides: test/CMakeFiles/testopt.dir/testopt.c.o.requires
	$(MAKE) -f test/CMakeFiles/testopt.dir/build.make test/CMakeFiles/testopt.dir/testopt.c.o.provides.build
.PHONY : test/CMakeFiles/testopt.dir/testopt.c.o.provides

test/CMakeFiles/testopt.dir/testopt.c.o.provides.build: test/CMakeFiles/testopt.dir/testopt.c.o


test/CMakeFiles/testopt.dir/__/src/util/timer.c.o: test/CMakeFiles/testopt.dir/flags.make
test/CMakeFiles/testopt.dir/__/src/util/timer.c.o: ../src/util/timer.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object test/CMakeFiles/testopt.dir/__/src/util/timer.c.o"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/testopt.dir/__/src/util/timer.c.o   -c /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/src/util/timer.c

test/CMakeFiles/testopt.dir/__/src/util/timer.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/testopt.dir/__/src/util/timer.c.i"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/src/util/timer.c > CMakeFiles/testopt.dir/__/src/util/timer.c.i

test/CMakeFiles/testopt.dir/__/src/util/timer.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/testopt.dir/__/src/util/timer.c.s"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/src/util/timer.c -o CMakeFiles/testopt.dir/__/src/util/timer.c.s

test/CMakeFiles/testopt.dir/__/src/util/timer.c.o.requires:

.PHONY : test/CMakeFiles/testopt.dir/__/src/util/timer.c.o.requires

test/CMakeFiles/testopt.dir/__/src/util/timer.c.o.provides: test/CMakeFiles/testopt.dir/__/src/util/timer.c.o.requires
	$(MAKE) -f test/CMakeFiles/testopt.dir/build.make test/CMakeFiles/testopt.dir/__/src/util/timer.c.o.provides.build
.PHONY : test/CMakeFiles/testopt.dir/__/src/util/timer.c.o.provides

test/CMakeFiles/testopt.dir/__/src/util/timer.c.o.provides.build: test/CMakeFiles/testopt.dir/__/src/util/timer.c.o


test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o: test/CMakeFiles/testopt.dir/flags.make
test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o: ../src/util/mt19937ar.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o   -c /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/src/util/mt19937ar.c

test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.i"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/src/util/mt19937ar.c > CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.i

test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.s"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/src/util/mt19937ar.c -o CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.s

test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o.requires:

.PHONY : test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o.requires

test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o.provides: test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o.requires
	$(MAKE) -f test/CMakeFiles/testopt.dir/build.make test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o.provides.build
.PHONY : test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o.provides

test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o.provides.build: test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o


test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o: test/CMakeFiles/testopt.dir/flags.make
test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o: ../src/util/nlopt-getopt.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o   -c /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/src/util/nlopt-getopt.c

test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.i"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/src/util/nlopt-getopt.c > CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.i

test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.s"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/src/util/nlopt-getopt.c -o CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.s

test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o.requires:

.PHONY : test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o.requires

test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o.provides: test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o.requires
	$(MAKE) -f test/CMakeFiles/testopt.dir/build.make test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o.provides.build
.PHONY : test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o.provides

test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o.provides.build: test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o


# Object files for target testopt
testopt_OBJECTS = \
"CMakeFiles/testopt.dir/testfuncs.c.o" \
"CMakeFiles/testopt.dir/testopt.c.o" \
"CMakeFiles/testopt.dir/__/src/util/timer.c.o" \
"CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o" \
"CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o"

# External object files for target testopt
testopt_EXTERNAL_OBJECTS =

test/testopt: test/CMakeFiles/testopt.dir/testfuncs.c.o
test/testopt: test/CMakeFiles/testopt.dir/testopt.c.o
test/testopt: test/CMakeFiles/testopt.dir/__/src/util/timer.c.o
test/testopt: test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o
test/testopt: test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o
test/testopt: test/CMakeFiles/testopt.dir/build.make
test/testopt: libnlopt.0.9.0.dylib
test/testopt: test/CMakeFiles/testopt.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Linking C executable testopt"
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/testopt.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/testopt.dir/build: test/testopt

.PHONY : test/CMakeFiles/testopt.dir/build

test/CMakeFiles/testopt.dir/requires: test/CMakeFiles/testopt.dir/testfuncs.c.o.requires
test/CMakeFiles/testopt.dir/requires: test/CMakeFiles/testopt.dir/testopt.c.o.requires
test/CMakeFiles/testopt.dir/requires: test/CMakeFiles/testopt.dir/__/src/util/timer.c.o.requires
test/CMakeFiles/testopt.dir/requires: test/CMakeFiles/testopt.dir/__/src/util/mt19937ar.c.o.requires
test/CMakeFiles/testopt.dir/requires: test/CMakeFiles/testopt.dir/__/src/util/nlopt-getopt.c.o.requires

.PHONY : test/CMakeFiles/testopt.dir/requires

test/CMakeFiles/testopt.dir/clean:
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test && $(CMAKE_COMMAND) -P CMakeFiles/testopt.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/testopt.dir/clean

test/CMakeFiles/testopt.dir/depend:
	cd /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/test /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test/CMakeFiles/testopt.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/testopt.dir/depend

