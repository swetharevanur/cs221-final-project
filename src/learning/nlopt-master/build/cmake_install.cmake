# Install script for directory: /Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/nlopt.pc")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/src/api/nlopt.h"
    "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/src/api/nlopt.hpp"
    "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/src/api/nlopt.f"
    )
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/libnlopt.0.9.0.dylib"
    "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/libnlopt.0.dylib"
    "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/libnlopt.dylib"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libnlopt.0.9.0.dylib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libnlopt.0.dylib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libnlopt.dylib"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      execute_process(COMMAND /usr/bin/install_name_tool
        -add_rpath "/usr/local/lib"
        "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/nlopt/NLoptLibraryDepends.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/nlopt/NLoptLibraryDepends.cmake"
         "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/CMakeFiles/Export/lib/cmake/nlopt/NLoptLibraryDepends.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/nlopt/NLoptLibraryDepends-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/nlopt/NLoptLibraryDepends.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/nlopt" TYPE FILE FILES "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/CMakeFiles/Export/lib/cmake/nlopt/NLoptLibraryDepends.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/nlopt" TYPE FILE FILES "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/CMakeFiles/Export/lib/cmake/nlopt/NLoptLibraryDepends-release.cmake")
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/nlopt" TYPE FILE FILES
    "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/NLoptConfig.cmake"
    "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/NLoptConfigVersion.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/src/api/cmake_install.cmake")
  include("/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/test/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/Users/KeanuSpies/Documents/2_Soph_2017/Fall/cs221/cs221-final-project/src/learning/nlopt-master/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")