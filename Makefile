.PHONY: build lint sign clean

build:
	python3 build.py

lint: build
	npx -y web-ext lint --source-dir dist --ignore-files '*.xpi'

# Requires AMO API credentials: https://addons.mozilla.org/developers/addon/api/key/
sign: build
	npx -y web-ext sign --channel=unlisted --source-dir dist --ignore-files '*.xpi' \
		--api-key "$$AMO_JWT_ISSUER" --api-secret "$$AMO_JWT_SECRET"

clean:
	rm -rf dist web-ext-artifacts
