from lean_dojo import LeanGitRepo, trace

repo = LeanGitRepo("https://github.com/lucyhorowitz/test", "3e6e7946d1c298b6a33158f18e217e94d90a5056")
trace(repo, dst_dir="traced_lean4-example")