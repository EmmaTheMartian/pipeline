-- add_rules("plugin.compile_commands.autoupdate", {outputdir = ".vscode"})
add_rules("plugin.compile_commands.autoupdate")
add_rules("mode.debug", "mode.release")
set_warnings("all", "error")
set_languages("c++17")
-- set_optimize("fastest")

add_requires("antlr4-runtime")

target("pipeline")
    set_kind("binary")
    add_packages("antlr4-runtime")
    add_deps("gen-syntax")
    add_headerfiles("src/generated/*.h")
    add_files("src/generated/*.cpp", "src/*.cpp")
target_end()

target("gen-syntax")
    set_kind("phony")
    on_run(function (target)
        if not os.exists("antlr-4.13.2-complete.jar") then
            os.exec("wget https://www.antlr.org/download/antlr-4.13.2.jar")
        end
        os.execv("java", {"-jar", "antlr-4.13.2-complete.jar", "-Dlanguage=Cpp", "-o", "src/generated/", "Language.g4"})
    end)
target_end()
