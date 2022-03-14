#!/bin/bash
function try()
{
    [[ $- = *e* ]]; SAVED_OPT_E=$?
    set +e
}

function throw()
{
    exit $1
}

function catch()
{
    export exception_code=$?
    (( $SAVED_OPT_E )) && set +e
    return $exception_code
}
echo "==> Installing dependencies..."
try
(
    echo "  -> Installing pypresence..."
    pip install pypresence > /dev/null
    echo "  -> Installed pypresence"
    echo "==> Complete! You can close this window now."
)
catch || {
   case $exc_code in
        *)
            echo "[!] Error occured while attempting to install dependencies, make sure Python is configured correctly."
            throw $exc_code
        ;;
    esac
}
