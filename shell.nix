{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
	buildInputs = with pkgs; [
		python3
		python3Packages.black
		pyright
	];

	shellHook = ''
		# Unset PYTHONPATH to avoid conflicts with nixpkgs python packages.
		unset PYTHONPATH

		python3 -m venv .venv
		source .venv/bin/activate
	'';
}
