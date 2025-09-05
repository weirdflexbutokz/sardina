# shell.nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python312
    pkgs.python312Packages.pip
    pkgs.python312Packages.questionary
    pkgs.python312Packages.tkinter
  ];

  shellHook = ''
    export UV_SYSTEM_PYTHON=1
  '';
}
