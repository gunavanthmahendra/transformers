from flask import Flask, render_template

app = Flask(__name__)

# Example SOP data with 4 levels
sop_data = {
    "Credit Card": {
        "Issuing": {
            "Application": {
                "Eligibility Check": "SOP details for credit card eligibility check."
            },
            "Dispatch": {
                "Card Creation": "SOP details for credit card creation and dispatch."
            }
        },
        "Usage": {
            "Domestic": {
                "Transaction Processing": "SOP for domestic credit card transactions."
            },
            "International": {
                "Transaction Processing": "SOP for international credit card transactions."
            }
        }
    },
    "Debit Card": {
        "Issuing": {
            "Application": {
                "Verification": "SOP for debit card application verification."
            },
            "Dispatch": {
                "Card Activation": "SOP for debit card activation."
            }
        },
        "Usage": {
            "ATM": {
                "Withdrawal": "SOP for ATM cash withdrawal using debit card."
            },
            "POS": {
                "Payments": "SOP for POS payments using debit card."
            }
        }
    },
    "NEFT": {
        "Initiation": {
            "Customer Request": {
                "Form Submission": "SOP for NEFT request form submission."
            },
            "Processing": {
                "Batch Scheduling": "SOP for NEFT batch scheduling."
            }
        },
        "Settlement": {
            "Bank Processing": {
                "Reconciliation": "SOP for NEFT settlement reconciliation."
            },
            "Notification": {
                "Customer Alert": "SOP for notifying customer of NEFT settlement."
            }
        }
    },
    "PPI": {
        "Issuing": {
            "KYC": {
                "Document Collection": "SOP for PPI KYC document collection."
            },
            "Wallet Creation": {
                "Setup": "SOP for creating a new PPI wallet."
            }
        },
        "Usage": {
            "Load Money": {
                "Limits": "SOP for loading money into PPI wallet."
            },
            "Payments": {
                "Merchant": "SOP for making merchant payments using PPI."
            }
        }
    },
    "PA-PG": {
        "Registration": {
            "Merchant Onboarding": {
                "Agreement": "SOP for PA-PG merchant onboarding agreement."
            },
            "Integration": {
                "API Setup": "SOP for PA-PG API integration setup."
            }
        },
        "Settlement": {
            "Payout": {
                "Schedule": "SOP for PA-PG payout schedule."
            },
            "Reporting": {
                "Reconciliation": "SOP for PA-PG reconciliation reporting."
            }
        }
    },
    "Merchant Acquiring Business (PoS, QR and Bharat QR)": {
        "Onboarding": {
            "KYC": {
                "Verification": "SOP for merchant KYC verification."
            },
            "Setup": {
                "Terminal Installation": "SOP for PoS terminal installation."
            }
        },
        "Transactions": {
            "POS": {
                "Processing": "SOP for processing PoS transactions."
            },
            "QR": {
                "Scanning": "SOP for scanning QR payments."
            }
        }
    },
    "UPI": {
        "Registration": {
            "User Creation": {
                "VPA Setup": "SOP for setting up UPI VPA."
            },
            "Linking": {
                "Bank Account": "SOP for linking bank account with UPI."
            }
        },
        "Transactions": {
            "P2P": {
                "Authorization": "SOP for UPI peer to peer authorization."
            },
            "P2M": {
                "Authorization": "SOP for UPI peer to merchant authorization."
            }
        }
    },
    "Bharat Connect (BBPS)": {
        "Onboarding": {
            "Biller Registration": {
                "Documentation": "SOP for BBPS biller registration documentation."
            },
            "API": {
                "Integration": "SOP for BBPS API integration."
            }
        },
        "Bill Payment": {
            "Customer": {
                "Validation": "SOP for BBPS customer validation."
            },
            "Settlement": {
                "Reporting": "SOP for BBPS settlement reporting."
            }
        }
    }
}

@app.route("/")
def index():
    return render_template("index.html", sop_data=sop_data)

if __name__ == "__main__":
    app.run(debug=True)
